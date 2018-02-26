import os
import subprocess
import configparser
import getpass
import pwd
import shutil
import dirsync
import copy
import glob

from .asset import Asset

class User:
    """Represent a single user's vsuite installation

    Track and manage vsuite's data files, user config, and more

    """

    def __init__(self):
        """Initialize vsuite object's constant attributes
        """
        self.user_config_dir = os.path.expanduser('~/.config/vsuite')
        self.user_config_file = os.path.join(self.user_config_dir, 'config.ini')
        self.user_data_dir = os.path.expanduser('~/.local/share/vsuite')
        self.user_project_skel = os.path.join(self.user_data_dir,'project_skel')
        self.user_project_files = os.path.join(self.user_data_dir,\
                'project_skel/project_files')
        self.user_csl = Asset('csl', 'csl', '*.csl', self.user_project_skel,\
                data_dir='project_files')
        self.user_templates = Asset('templates', 'templates', '*.j2',\
                self.user_project_skel, data_dir='project_files')
        self.user_bibliographies = Asset('bibliographies', '..', '*.bib',\
                self.user_project_skel, data_dir='project_files')
        self.user_makefile = Asset('makefile', '.', 'makefile',\
                self.user_project_skel, data_dir='project_files')
        self.user_config = Asset('config', '.', 'config.ini',\
                self.user_config_dir, data_dir='')
        self.user_assets = [self.user_csl, self.user_templates,\
                self.user_bibliographies, self.user_config, self.user_makefile]

    def user_init(self):
        """Ensure existence of user config and user data
        """
        self.get_user_config()
        self.init_project_skel()

    def init_project_skel(self):
        """Create user data from vsuite skeleton
        """
        app_skel = os.path.join(os.path.dirname(__file__), 'project_skel')
        app_assets = [copy.deepcopy(asset) for asset in self.user_assets]
        for i in range(len(app_assets)):
            app_assets[i].project_path = app_skel
            app_assets[i].project_dir = '.vsuite'
            self.copy_asset(app_assets[i], self.user_assets[i])

    def get_user_config(self):
        """Get user's user vsuite config

        Get existing config if it exists
        Get and save newly-generated config if it doesn't

        Returns:
            configparser.ConfigParser: user's user configuration

        """
        if os.path.exists(self.user_config_file):
            config = self.read_user_config()
        else:
            config = self.init_user_config()
        return config

    def init_user_config(self):
        """Initialize user config

        Create new config, refusing to overwrite existing one

        Returns:
            configparser.ConfigParser: user's user configuration

        """
        config = configparser.ConfigParser()
        config['default'] = {
                'csl': 'chicago-fullnote-bibliography-with-ibid.csl',
                'author': self.get_fullname(),
                'bibliography': 'bibliography.bib',
                'template': 'default.j2'}
        # Write user_config_file in user_config_dir
        if not os.path.exists(self.user_config_dir):
            os.makedirs(self.user_config_dir)
        with open(self.user_config_file, 'w') as configfile:
            config.write(configfile)
        return config

    def get_fullname(self):
        """Get user's full name from /etc/passwd

        Returns:
            str: user's full name

        """
        username = getpass.getuser()
        pwuser = pwd.getpwnam(username)
        username = pwuser.pw_gecos
        # Ignore commas that come from password file
        username = username.replace(",","")
        return username

    def read_user_config(self):
        """Get existing user config
        """
        config = configparser.ConfigParser()
        config.read(self.user_config_file)
        return config

    def copy_asset(self, src_asset, dest_asset):
        """Copy asset files from one asset to another

        Args:
            src_asset (vsuite.asset.Asset): asset to be copied
            dest_asset (vsuite.asset.Asset): asset to receive files

        """
        assert (src_asset.name == dest_asset.name),\
                'Not copying %s into %s' % (src_asset.name, dest_asset.name)
        src_dir = src_asset.abspath()
        dest_dir = dest_asset.abspath()
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        files = glob.glob(os.path.join(src_dir,src_asset.file_expression))
        [shutil.copy2(file, dest_dir) for file in files]
