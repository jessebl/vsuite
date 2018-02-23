#!/usr/bin/env python3
import argparse
import sys
import os
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
    parser_csl = subparsers.add_parser('csl',\
            help='list available csl files')
    parser_new = subparsers.add_parser('new',\
            help='create new doc from template')
    parser_make = subparsers.add_parser('make',\
            help='make document from markdown file')
    # Capital G since 'global' is a keyword which makes args.global is invalid
    parser_init.add_argument('-u', '--user',\
            help='initialize user config',\
            action='store_true')
    parser_init.add_argument('-i', '--inherit',\
            help='inherit data and config from parent project',\
            action='store_true')
    parser_new.add_argument('title',\
            help='document title')
    parser_new.add_argument('-t', '--template',\
            help='template file to use from template directory')
    parser_make.add_argument('output',\
            help='document name with desired file extension')
    args = parser.parse_args()
    return (args, parser)

def main():
    """
    Respond to subcommands, exit with code 127 without subcommands
    """
    project_instance = Project()
    args, parser = parse_args()
    if args.subcommand == 'init':
        if args.user:
            project_instance.__init__(path=os.getcwd())
            project_instance.user_init()
        elif args.inherit:
            project_instance.__init__(path=os.getcwd())
            project_instance.init_inherit()
        else:
            project_instance.init()
    elif args.subcommand == 'csl':
        project_instance.csl.print_files()
    elif args.subcommand == 'new':
        title = args.title
        template = args.template
        project_instance.create_doc(title, template)
    elif args.subcommand == 'make':
        output = args.output
        project_instance.make(output)
    else:
        parser.print_help()
        sys.exit(127)

if __name__ == '__main__':
    main()
