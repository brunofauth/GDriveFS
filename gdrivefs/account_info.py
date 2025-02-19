import logging

from gdrivefs.livereader_base import LiveReaderBase
from gdrivefs.drive import get_gdrive

_logger = logging.getLogger(__name__)


class AccountInfo(LiveReaderBase):
    """Encapsulates our account info."""

    __map = {'root_id': 'rootFolderId',
             'largest_change_id': ('largestChangeId', int),
             'quota_bytes_total': ('quotaBytesTotal', int),
             'quota_bytes_used': ('quotaBytesUsed', int)}

    def get_data(self):
        gd = get_gdrive()
        return gd.get_about_info()

    def __getattr__(self, key):
        target = AccountInfo.__map[key]
        _type = None

        if target.__class__ == tuple:
            (target, _type) = target

        value = self[target]
        if _type is not None:
            value = _type(value)

        return value

    @property
    def keys(self):
        return list(AccountInfo.__map.keys())

