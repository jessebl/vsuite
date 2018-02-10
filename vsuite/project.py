import os
import subprocess
import configparser
from .user import User

class Project(User):

    def __init__(self):
        """
        Initialize vsuite for inheritance
        """
        self.project_path = os.getcwd()
        self.project_dir = os.path.join(self.project_path, '.vsuite')
        self.project_config = os.path.join(self.project_dir, 'config.ini')
        User.__init__(self)

    def init(self):
        """
        Initialize project
        """
        self.global_init()
        self.git_init()
        self.create_project_dir()

    def git_init(self):
        """
        Initialize and configure git repository in project_path
        """
        cmd = ['git', 'init']
        subprocess.run(cmd, cwd=self.project_path)

    def create_project_dir(self):
        """
        Create vsuite hidden project folder
        Includes csl files
        Do nothing if directory already exists
        """
        if not os.path.exists(self.project_dir):
            os.makedirs(self.project_dir)
            self.init_project_config()
        else:
            return

    def init_project_config(self):
        """
        Copy user config into project
        """
        config = configparser.ConfigParser()
        config.read(self.global_config_file)
        with open(self.project_config, 'w') as configfile:
            config.write(configfile)

    def copy_skel(self):
        """
        Copy skel directory to new project
        """
        pass
