import logging
from googleapiclient.discovery import DISCOVERY_URI

_logger = logging.getLogger(__name__)

# TODO(dustin): Move this module to the *config* directory, eliminate this
#               class, and use the module directly.

SCOPE = ["https://www.googleapis.com/auth/drive"]


class Conf(object):
    """Manages options."""

    auth_cache_filepath                 = None
#    gd_to_normal_mapping_filepath       = '/etc/gdfs/mime_mapping.json'
    extension_mapping_filepath          = '/etc/gdfs/extension_mapping.json'
    query_decay_intermed_prefix_length  = 7
    file_jobthread_max_idle_time        = 60
    file_chunk_size_kb                  = 1024
    file_download_temp_max_age_s        = 86400
    change_check_frequency_s            = 3
    hidden_flags_list_local             = ['trashed', 'restricted']
    hidden_flags_list_remote            = ['trashed']
    cache_cleanup_check_frequency_s     = 60
    cache_entries_max_age               = 8 * 60 * 60
    cache_status_post_frequency_s       = 10

# Deimplementing report functionality.
#    report_emit_frequency_s             = 60

    google_discovery_service_url        = DISCOVERY_URI
    default_buffer_read_blocksize       = 65536
    directory_mimetype                  = 'application/vnd.google-apps.folder'
    default_perm_folder                 = '777'
    default_perm_file_editable          = '666'
    default_perm_file_noneditable       = '444'

    # How many extra entries to retrieve when an entry is accessed that is not
    # currently cached.
    max_readahead_entries = 10

    use_pass: bool                      = False

    @staticmethod
    def get(key):
        return Conf.__dict__[key]

    @staticmethod
    def set(key, value):
        if key not in Conf.__dict__:
            raise KeyError(key)

        setattr(Conf, key, value)


