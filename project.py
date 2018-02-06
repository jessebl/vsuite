import os
import subprocess
import configparser
import getpass
import pwd

class Project:

    def __init__(self):
        """
        Create vsuite config if it doesn't exist
        """
        self.project_path = os.getcwd()
        self.global_config_dir = os.path.expanduser('~/.config/vsuite')
        self.global_config_file = os.path.join(self.global_config_dir, 'config.ini')
        self.global_config = self.get_global_config()

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
        #

    def get_global_config(self):
        """
        Return existing config if it exists
        Return and save newly-generated config if it doesn't
        """
        if os.path.exists(self.global_config_file):
            config = self.read_global_config()
        else:
            config = self.init_global_config()
        return config

    def init_global_config(self):
        """
        Create global_config_dir if it doesn't exist, and global_config_file
        """
        config = configparser.ConfigParser()
        config['default'] = {'csl': 'chicago',
                'author': self.get_fullname()}
        # Write global_config_file in global_config_dir
        if not os.path.exists(self.global_config_dir):
            os.makedirs(self.global_config_dir)
        with open(self.global_config_file, 'w') as configfile:
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

    def read_global_config(self):
        """
        Return existing config
        """
        config = configparser.ConfigParser()
        config.read(self.global_config_file)
        return config

    def copy_skel(self):
        """
        Copy skel directory to new project
        """
        pass
