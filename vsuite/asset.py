import os
import glob

class Asset():
    """Represent a category of vsuite assets

    Args:
        relpath (str): path to assset directory relative to .vsuite
        file_expression (str): expression to match asset files,
            parsed by glob.glob
        project_path (str): path to project
        data_dir (str): directory within ``project_path`` to hold data files
            (``.vsuite``, leave unless you know what you're doing)

    """

    def __init__(self, name, relpath, file_expression, project_path,\
            data_dir='.vsuite'):
        self.name = name
        self.relpath = relpath
        self.file_expression = file_expression
        self.project_path = project_path
        self.project_dir = data_dir

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
        relpath = os.path.relpath(self.abspath(), os.getcwd())
        return relpath

    def abspaths(self):
        """Paths of available assets

        Get absolute paths of asset files in first level of asset directory

        Returns:
            tuple: file paths

        """
        file_pattern = os.path.join(self.abspath(), self.file_expression)
        files = glob.glob(file_pattern)
        return tuple(files)

    def files(self):
        """Available asset files

        Get asset filenames in first level of asset directory

        Returns:
            tuple: asset filenames
        """
        files = [os.path.basename(filepath) for filepath in self.abspaths()]
        return tuple(files)

    def print_files(self):
        """Print asset files, newline delimitedfile names
        """
        [print(asset_file) for asset_file in self.files()]
