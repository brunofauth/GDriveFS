#!/usr/bin/env python

import sys
import os.path
dev_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, dev_path)

import logging
import os.path
import webbrowser
import argparse

import gdrivefs.conf
import gdrivefs.config
import gdrivefs.config.log
import gdrivefs.gdfuse
import gdrivefs.oauth_authorize
import gdrivefs.auto_auth

_logger = logging.getLogger(__name__)


def _handle_auth_url():
    oa = gdrivefs.oauth_authorize.OauthAuthorize()
    url = oa.step1_get_auth_url()

    print("To authorize FUSE to use your Google Drive account, visit the "
          "following URL to produce an authorization code:\n\n%s\n" %
          (url,))


def _auth_write(authcode):
    oa = gdrivefs.oauth_authorize.OauthAuthorize() # It's this class that has to be changed to support 'pass'
    oa.step2_doexchange(authcode)

    print("Authorization code recorded.")


def _handle_auth_automatic():
    aa = gdrivefs.auto_auth.AutoAuth()
    aa.get_and_write_creds()

    print("Authorization code recorded.")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', action='store_true', help='Print logging')
    parser.add_argument("mode", choices=["auth_get_url", "auth_write", "auth_automatic"])
    parser.add_argument("-c", '--code', help="For 'auth_write' only (but everytime)")
    parser.add_argument("-p", '--use-pass', action="store_true", help="Store credentials in a pass keys, instead of json file.")
    parser.add_argument("-s", "--storage-path", help="Where to put the json file or pass key",
            default=gdrivefs.config.DEFAULT_CREDENTIALS_FILEPATH)
    args = parser.parse_args()

    gdrivefs.config.log.configure(is_debug=args.verbose)
    gdrivefs.conf.Conf.set("use_pass", args.use_pass)
    gdrivefs.gdfuse.set_auth_cache_filepath(args.storage_path)

    if args.mode == 'auth_get_url':
        return _handle_auth_url()
    if args.mode == 'auth_write':
        return _auth_write(args.code)
    if args.mode == 'auth_automatic':
        return _handle_auth_automatic()


if __name__ == '__main__':
    main()

