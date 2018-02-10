#!/usr/bin/env python3
import argparse
import sys
from .project import Project

def parse_args():
    """
    Parse arguments and subcommands
    """
    parser = argparse.ArgumentParser(\
            description='Plaintext project management for those who want a\
            clean and powerful workflow')
    subparsers = parser.add_subparsers(dest='subcommand')
    parser_init = subparsers.add_parser('init',\
            help='initialize vsuite in current directory')
    parser_init = subparsers.add_parser('csl',\
            help='list available csl files')
    # Capital G since 'global' is a keyword which makes args.global is invalid
    parser_init.add_argument('-G', '--Global',\
            help='initialize global config',\
            action='store_true')
    args = parser.parse_args()
    return (args, parser)

def main():
    """
    Respond to subcommands, exit with code 127 without subcommands
    """
    project_instance = Project()
    args, parser = parse_args()
    if args.subcommand == 'init':
        if args.Global:
            project_instance.global_init()
        else:
            project_instance.init()
    elif args.subcommand == 'csl':
        project_instance.print_csl()
    else:
        parser.print_help()
        sys.exit(127)

if __name__ == '__main__':
    main()