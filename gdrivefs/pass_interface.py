import subprocess as sp
import os

from glob import glob
from typing import Any

from oauth2client.client import UnknownClientSecretsFlowError, OAuth2WebServerFlow
from oauth2client.clientsecrets import _validate_clientsecrets, TYPE_WEB, TYPE_INSTALLED


def _list_stored_passwords(root: str) -> list[str]:
    return glob("**/*.gpg", root_dir=root)


def get_pass_data(key: str) -> str:

    pw_store_dir = os.environ.get("PASSWORD_STORE_DIR", None)
    if pw_store_dir is None:
        raise OSError("'PASSWORD_STORE_DIR' environment variable isn't set")
    if key + ".gpg" not in _list_stored_passwords(pw_store_dir):
        raise ValueError(f"There's no password stored under the name {key!r}")

    process = sp.run(["pass", key], check=True, text=True, capture_output=True)
    return process.stdout


def set_pass_data(key: str, value: str) -> None:
    sp.run(["pass", "insert", "--multiline", key], input=value, check=True, text=True)


def del_pass_data(key: str) -> None:
    sp.run(["pass", "rm", key], check=True, text=True)


def flow_from_clientsecrets_json(secrets_json: dict[str, Any], scope) -> OAuth2WebServerFlow:
    """Create a Flow from a clientsecrets file.

    Will create the right kind of Flow based on the contents of the
    clientsecrets file or will raise InvalidClientSecretsError for unknown
    types of Flows.

    Args:
        filename: string, File name of client secrets.
        scope: string or iterable of strings, scope(s) to request.

    Returns:
        A Flow object.

    Raises:
        UnknownClientSecretsFlowError: if the file describes an unknown kind of Flow.
        InvalidClientSecretsError: if the clientsecrets file is invalid.
    """
    client_type, client_info = _validate_clientsecrets(secrets_json)
    if client_type not in (TYPE_WEB, TYPE_INSTALLED):
        raise UnknownClientSecretsFlowError(f'This OAuth 2.0 flow is unsupported: {client_type!r}')

    constructor_kwargs = {
        'redirect_uri': None,
        'auth_uri': client_info['auth_uri'],
        'token_uri': client_info['token_uri'],
        'login_hint': None}

    if (revoke_uri := client_info.get('revoke_uri')) is not None:
        constructor_kwargs["revoke_uri"] = revoke_uri

    return OAuth2WebServerFlow(
        client_info['client_id'], client_info['client_secret'],
        scope, **constructor_kwargs)


def flow_from_pass(key: str, scope: list[str]) -> OAuth2WebServerFlow:
    return flow_from_clientsecrets_json(json.loads(get_pass_data(key)), scope)

