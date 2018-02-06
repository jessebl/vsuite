#!/usr/bin/env python3
import project
import argparse
import sys

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
    args = parser.parse_args()
    return (args, parser)

def main():
    """
    Respond to subcommands, exit with code 127 without subcommands
    """
    project_instance = project.Project()
    args, parser = parse_args()
    if args.subcommand == 'init':
        project_instance.init()
    else:
        parser.print_help()
        sys.exit(127)

if __name__ == '__main__':
    main()
