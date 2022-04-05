import os
from pathlib import Path

IS_DEBUG = bool(int(os.environ.get('GD_DEBUG', '0')))
DO_LOG_FUSE_MESSAGES = bool(int(os.environ.get('GD_DO_LOG_FUSE_MESSAGES', '0')))

DEFAULT_CREDENTIALS_DIR = Path(os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share/gdfs")))
DEFAULT_CREDENTIALS_DIR.mkdir(exist_ok=True)
DEFAULT_CREDENTIALS_FILEPATH = DEFAULT_CREDENTIALS_DIR / "credentials.json"

