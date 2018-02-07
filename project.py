import os
import subprocess
import configparser
from vsuite import VSuite

class Project(VSuite):

    def __init__(self):
        """
        Initialize vsuite for inheritance
        """
        self.project_path = os.getcwd()
        VSuite.__init__(self)

    def init(self):
        """
        Initialize project
        """
        self.global_init()
        self.git_init()
        self.copy_skel()

    def git_init(self):
        """
        Initialize and configure git repository in project_path
        """
        cmd = ['git', 'init']
        subprocess.run(cmd, cwd=self.project_path)

    def copy_skel(self):
        """
        Copy skel directory to new project
        """
        pass
