class GdFsError(Exception):
    pass


class AuthorizationError(GdFsError):
    """All authorization-related errors inherit from this."""


class AuthorizationFailureError(AuthorizationError):
    """There was a general authorization failure."""


class AuthorizationFaultError(AuthorizationError):
    """Our authorization is not available or has expired."""


class MustIgnoreFileError(GdFsError):
    """An error requiring us to ignore the file."""


class FilenameQuantityError(MustIgnoreFileError):
    """Too many filenames share the same name in a single directory."""


class ExportFormatError(GdFsError):
    """A format was not available for export."""


class GdNotFoundError(GdFsError):
    """A file/path was not found."""
