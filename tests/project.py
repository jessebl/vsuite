import os
import tempfile
import unittest

from vsuite.project import Project

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.project_dir = tempfile.mkdtemp()
        os.chdir(self.project_dir)
        self.project = Project()

    def test_init(self):
        self.project.init()
        self.init_project_assets()

    def init_project_assets(self):
        paths = {}
        paths['git_path'] = os.path.join(self.project_dir, '.git')
        paths['vsuite_dir'] = os.path.join(self.project_dir,\
                '.vsuite')
        paths['csl'] = os.path.join(paths['vsuite_dir'], 'csl')
        paths['templates'] = os.path.join(paths['vsuite_dir'], 'templates')
        paths['config'] = os.path.join(paths['vsuite_dir'], 'config.ini')
        paths['bibliography'] = os.path.join(self.project_dir,\
                'bibliography.bib')
        paths['git'] = os.path.join(self.project_dir, '.git')
        for path in paths:
            self.assertTrue(os.path.exists(paths[path]),\
                    msg=str(paths[path]+' does not exist'))

if __name__ == '__main__':
    unittest.main()
