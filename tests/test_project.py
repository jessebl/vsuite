import os
import tempfile
import unittest
import shutil
import subprocess

from vsuite.project import Project

class ProjectTestCase(unittest.TestCase):
    def setUp(self):
        """Initialize project as attribute
        """
        self.project_dir = tempfile.mkdtemp()
        os.chdir(self.project_dir)
        self.project = Project()
        self.project.init()

    def test_init_project_assets(self):
        """Initialize project assets
        """
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
        """Create document in project root
        """
        doc = self.create_doc()
        self.make_doc(doc)

    def test_create_doc_subdir(self):
        """Create document in project subdirectory
        """
        subdir = 'subdir'
        os.mkdir(subdir)
        os.chdir(subdir)
        # Check if same project is still recognized
        self.assertEqual(self.project.project_path, self.project_dir)
        # Ensure document creation works
        doc = self.create_doc()
        self.make_doc(doc)

    def create_doc(self):
        title = 'test_doc'
        filename = self.project.create_doc(title)
        return filename

    def make_doc(self, filename):
        if not os.getenv('TEST_MAKE') == '0':
            target = os.path.splitext(filename)[0]
            print('making', target)
            cmd = ['pandoc', filename, '-o', target+'.odt']
            with open(os.devnull, 'w') as fp:
                subprocess.run(cmd, stdout=fp)

    def test_no_user_config(self):
        """Create working project while user config missing
        """
        config_file = os.path.expanduser('~/.config/vsuite/config.ini')
        os.remove(config_file)
        self.project.init()
        doc = self.create_doc()
        self.make_doc(doc)

    def test_create_doc_no_project(self):
        """Document creation fails outside of project
        """
        project_files = os.path.join(self.project_dir, '.vsuite')
        shutil.rmtree(project_files)
        try:
            self.create_doc()
        except FileExistsError:
            excepted = True
        self.assertTrue(excepted,msg='create_doc() succeeds outside of project')

if __name__ == '__main__':
    unittest.main()
