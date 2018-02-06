#!/usr/bin/env python3
import os
import subprocess
import argparse
import configparser
import getpass
import pwd
import sys

class Project:

    def __init__(self):
        """
        Create vsuite config if it doesn't exist
        """
        self.project_path = os.getcwd()
        self.user_config_dir = os.path.expanduser('~/.config/vsuite')
        self.user_config_file = os.path.join(self.user_config_dir, 'config.ini')
        self.user_config = self.get_user_config()

    def init(self):
        """
        Initialize project
        """
        self.git_init()
        self.copy_skel()

    def git_init(self):
        """
        Initialize and configure git repository in project_path
        """
        cmd = ['git', 'init']
        subprocess.run(cmd, cwd=self.project_path)

    def get_user_config(self):
        """
        Return existing config if it exists
        Return and save newly-generated config if it doesn't
        """
        if os.path.exists(self.user_config_file):
            config = self.read_user_config()
        else:
            config = self.init_user_config()
        return config

    def init_user_config(self):
        """
        Create user_config_dir if it doesn't exist, and user_config_file
        """
        config = configparser.ConfigParser()
        config['default'] = {'csl': 'chicago',
                'author': self.get_fullname()}
        # Write user_config_file in user_config_dir
        if not os.path.exists(self.user_config_dir):
            os.makedirs(self.user_config_dir)
        with open(self.user_config_file, 'w') as configfile:
            config.write(configfile)
        return config

    def get_fullname(self):
        """
        Return user's full name from /etc/passwd
        """
        username = getpass.getuser()
        pwuser = pwd.getpwnam(username)
        username = pwuser.pw_gecos
        # Ignore commas that come from password file
        username = username.replace(",","")
        return username

    def read_user_config(self):
        """
        Return existing config
        """
        config = configparser.ConfigParser()
        config.read(self.user_config_file)
        return config

    def copy_skel(self):
        """
        Copy skel directory to new project
        """
        pass


def parse_args():
    """
    Parse arguments and subcommands
    """
    parser = argparse.ArgumentParser(\
            description='A plaintext project management system aimed at \
            students who want a clean and powerful workflow')
    subparsers = parser.add_subparsers(dest='subcommand')
    parser_init = subparsers.add_parser('init',\
            help='initialize vsuite in current directory')
    args = parser.parse_args()
    return (args, parser)

def main():
    """
    Respond to subcommands, exit with code 127 without subcommands
    """
    project = Project()
    args, parser = parse_args()
    if args.subcommand == 'init':
        project.init()
    else:
        parser.print_help()
        sys.exit(127)

if __name__ == '__main__':
    main()
