import os
import tempfile
import unittest

from vsuite.project import Project

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        self.project_dir = tempfile.mkdtemp()
        os.chdir(self.project_dir)
        self.project = Project()
        self.project.init()

    def test_init(self):
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
        paths['makefile'] = os.path.join(paths['vsuite_dir'], 'makefile')
        for path in paths:
            self.assertTrue(os.path.exists(paths[path]),\
                    msg=str(paths[path]+' does not exist'))

    def test_create_doc(self):
        doc = self.create_doc()

    def test_create_doc_subdir(self):
        subdir = 'subdir'
        os.mkdir(subdir)
        os.chdir(subdir)
        # Check if same project is still recognized
        self.assertEqual(self.project.project_path, self.project_dir)
        # Ensure document creation works
        doc = self.create_doc()

    def create_doc(self):
        title = 'test_doc'
        self.project.create_doc(title)
        return title

if __name__ == '__main__':
    unittest.main()
