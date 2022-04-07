#!/usr/bin/env python

import sys
import os.path
dev_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, dev_path)

import argparse

import gdrivefs.conf
import gdrivefs.config.log
import gdrivefs.volume
import gdrivefs.fsutility
import gdrivefs.gdfuse
import gdrivefs.errors


def _get_by_path(raw_path):
    result = gdrivefs.fsutility.split_path(raw_path, gdrivefs.volume.path_resolver)
    (parent_clause, path, filename, mime_type, is_hidden) = result

    filepath = gdrivefs.fsutility.build_filepath(path, filename)
    path_relations = gdrivefs.volume.PathRelations.get_instance()
    entry_clause = path_relations.get_clause_from_path(filepath)

    return entry_clause[gdrivefs.volume.CLAUSE_ENTRY]


def _get_by_id(_id):
    cache = gdrivefs.volume.EntryCache.get_instance().cache
    return cache.get(_id)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cred_filepath', help='Credentials file')
    parser.add_argument("-p", '--use-pass', action="store_true", help="Store credentials in a pass keys, instead of json file")
    parser.add_argument("entry-path", help="Path to resource")
    parser.add_argument("-i", "--use-id", action="store_true", help="Treat 'entry-path' as the resources' id, instead of path")

    args = parser.parse_args()

    gdrivefs.conf.Conf.set("use_pass", args.use_pass)
    gdrivefs.gdfuse.set_auth_cache_filepath(args.cred_filepath)

    entry = (_get_by_id if args.use_id else _get_by_path)(args.entry_path)
    print(entry)
    print()

    for _type, _dict in data.get_data().iteritems():
        print("[%s]\n" % (_type))

        for key, value in _dict.iteritems():
            print("%s: %s" % (key, value))

        print()


if __name__ == '__main__':
    main()
