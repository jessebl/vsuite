import os
import glob

class Asset():
    """Represent a category of vsuite assets
    """

    def __init__(self, relpath, file_extension, project_path):
        """

        Args:
            relpath (str): path to assset directory relative to .vsuite
            file_extension (str): file extension of assets

        """
        self.relpath = relpath
        self.file_extension = file_extension
        self.project_path = project_path
        self.project_dir = '.vsuite'

    def abspath(self):
        """Get absolute path to asset

        Args:
            project_path (str): absolute path to project

        Returns:
            str: absolute path to asset
        """
        abspath = os.path.join(self.project_path,\
                self.project_dir, self.relpath)
        return abspath

    def relpath_pwd(self):
        """Get path to asset relative to current directory

        Args:
            project_dir (str): absolute path to project directory

        Returns:
            str: relative path to asset
        """
        abspath = self.abspath(project_dir)
        relpath = os.path.relpath(abspath, os.getcwd())
        return relpath
