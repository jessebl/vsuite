import os
import tempfile
import unittest

from vsuite.project import Project

class AssetTestCase(unittest.TestCase):
    def setUp(self):
        self.project_dir = tempfile.mkdtemp()
        os.chdir(self.project_dir)
        self.project = Project()
        self.project.init()

    def test_asset_csl_files(self):
        """Find CSL path in project
        """
        self.project.csl.abspaths()

if __name__ == '__main__':
    unittest.main()
