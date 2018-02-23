import os
import shutil
import unittest

from vsuite.user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_copy_project_skel(self):
        """Initialize user data
        """
        project_skel_dest = os.path.expanduser('~/.local/share/vsuite/'
                'project_skel')
        if os.path.exists(project_skel_dest):
            shutil.rmtree(project_skel_dest)
        self.user.init_project_skel()
        paths = {}
        paths['vsuite_dir'] = os.path.join(project_skel_dest,\
                'project_files')
        paths['csl'] = os.path.join(paths['vsuite_dir'], 'csl')
        paths['templates'] = os.path.join(paths['vsuite_dir'], 'templates')
        paths['bibliography'] = os.path.join(project_skel_dest,\
                'bibliography.bib')
        paths['makefile'] = os.path.join(paths['vsuite_dir'], 'makefile')
        for path in paths:
            self.assertTrue(os.path.exists(paths[path]),\
                    msg=str(paths[path]+' does not exist'))

    def test_get_user_config(self):
        """Get user config
        """
        config_path = os.path.expanduser('~/.config/vsuite/config.ini')
        if os.path.exists(config_path):
            os.remove(config_path)
        self.user.get_user_config()
        self.assertTrue(os.path.exists(config_path))

if __name__ == '__main__':
    unittest.main()
