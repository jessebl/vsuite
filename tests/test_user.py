import os
import shutil
import unittest

from vsuite.user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_global_init(self):
        data_dir = os.path.expanduser('~/.local/share/vsuite')
        if os.path.exists(data_dir):
            shutil.rmtree(data_dir)
        self.user.global_init()
        paths = {}
        paths['vsuite_dir'] = os.path.expanduser('~/.local/share/'
                'vsuite/project_files')
        paths['csl'] = os.path.join(paths['vsuite_dir'], 'csl')
        paths['templates'] = os.path.join(paths['vsuite_dir'], 'templates')
        for path in paths:
            self.assertTrue(os.path.exists(paths[path]),\
                    msg=str(paths[path]+' does not exist'))

if __name__ == '__main__':
    unittest.main()
