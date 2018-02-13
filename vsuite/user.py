import os
import subprocess
import configparser
import getpass
import pwd
import shutil
import dirsync

class User:

    def __init__(self):
        """
        Initialize vsuite object's constant attributes
        """
        self.global_config_dir = os.path.expanduser('~/.config/vsuite')
        self.global_config_file = os.path.join(self.global_config_dir, 'config.ini')
        self.global_data_dir = os.path.expanduser('~/.local/share/vsuite')
        self.global_project_files = os.path.join(self.global_data_dir,\
                'project_files')

    def global_init(self):
        """
        Load global config after creating it if it doesn't exist
        """
        self.global_config = self.get_global_config()
        self.init_global_data_dir()

    def init_global_data_dir(self):
        """
        Copy project files to data dir
        """
        project_files_path = os.path.join(os.path.dirname(__file__),\
                'project_files')
        # Create dummy method with info() method to supress dirsync output...
        dummy_function = lambda x : None
        dummy_logger = type('Dummy', (object,), {'info': dummy_function})
        dirsync.sync(project_files_path, self.global_project_files, 'sync',\
                logger=dummy_logger, create=True)

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
        config['default'] = {
                'csl': 'chicago-fullnote-bibliography-with-ibid.csl',
                'author': self.get_fullname(),
                'bibliography': 'bibliography.bib',
                'template': 'default.j2'}
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
