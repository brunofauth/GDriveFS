#!/usr/bin/env python

import sys
import os.path
dev_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, dev_path)

import logging
import argparse

import gdrivefs.config
import gdrivefs.config.log
import gdrivefs.gdfuse

_logger = logging.getLogger(__name__)


def _main():
    p = argparse.ArgumentParser()

    p.add_argument('mountpoint', help='Mount point')
    p.add_argument("-c", '--credentials', help="Credentials file or pass key", default=gdrivefs.config.DEFAULT_CREDENTIALS_FILEPATH)
    p.add_argument("-p", "--use-pass", action="store_true", help="Load credentials not from disk, but 'pass'")

    p.add_argument('-v', '--verbose', action='store_true')
    p.add_argument('-o', '--mount-options', help='Mount options')
    
    p.add_argument('-f', '--dry-run', action='store_true', help="Parse args and exit (required by 'mount' command)")
    p.add_argument('-n', '--no-mtab', action='store_true', help="Unused (required by 'mount' command)")

    args = p.parse_args()

    gdrivefs.config.log.configure(is_debug=args.verbose)

    option_string = args.mount_options[0] if args.mount_options else None

    _logger.debug("Mounting GD with creds at [%s]: %s", args.credentials, args.mountpoint)
    if args.dry_run:
        _logger.warning("'Fake' mount. Exiting successfully.")
        return

    gdrivefs.gdfuse.mount(
        auth_storage_filepath=args.credentials,
        use_pass=args.use_pass,
        mountpoint=args.mountpoint,
        debug=gdrivefs.config.IS_DEBUG,
        nothreads=gdrivefs.config.IS_DEBUG,
        option_string=option_string)


if __name__ == '__main__':
    _main()
