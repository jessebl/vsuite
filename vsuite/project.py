import os
import subprocess
import configparser
import shutil
import jinja2
import dirsync
import glob
from .user import User

class Project(User):

    def __init__(self):
        """
        Initialize vsuite for inheritance
        """
        # self.project_path is absolute
        self.project_path = self.get_project_dir()
        self.project_dir = os.path.join(self.project_path, '.vsuite')
        self.project_config = os.path.join(self.project_dir, 'config.ini')
        self.project_csl_dir = os.path.join(self.project_dir, 'csl')
        self.project_template_dir = os.path.join(self.project_dir, 'templates')
        # dict of paths relative to project_dir
        self.relpaths_project = {'project': '.',\
                'csl_dir': 'csl',\
                'template_dir': 'templates',\
                'bibliography_dir': os.pardir}
        self.abspaths = self.get_abspaths()
        self.relpaths_pwd = self.get_relpaths()
        User.__init__(self)

    def init(self):
        """
        Initialize project
        """
        self.global_init()
        self.git_init()
        self.create_project_dir()
        self.create_bibliography()


    def create_bibliography(self):
        """
        Create bibliography if it doesn't exist
        """
        config = configparser.ConfigParser()
        config.read(self.project_config)
        bibliography_file = config['default']['bibliography']
        if not os.path.exists(bibliography_file):
            with open(bibliography_file, 'w') as bib:
                bib.write('')

    def git_init(self):
        """
        Initialize and configure git repository in project_path
        """
        cmd = ['git', 'init']
        with open(os.devnull, 'w') as fp:
            subprocess.run(cmd, cwd=self.project_path, stdout=fp)

    def create_project_dir(self):
        """
        Create vsuite hidden project folder with project files
        Do nothing if directory already exists
        """
        # Create dummy method with info() method to supress dirsync output...
        dummy_function = lambda x : None
        dummy_logger = type('Dummy', (object,), {'info': dummy_function})
        dirsync.sync(self.global_project_files, self.project_dir, 'sync',\
                logger=dummy_logger, create=True)
        self.init_project_config()

    def init_project_config(self):
        """
        Copy user config into project
        """
        config = configparser.ConfigParser()
        config.read(self.global_config_file)
        with open(self.project_config, 'w') as configfile:
            config.write(configfile)

    def check_for_project(self):
        """
        Verify that current directory is a project
        """
        if not os.path.exists(self.project_dir):
            raise FileExistsError('Not in a vsuite project')

    def create_doc(self, title, template_opt=None):
        """
        Create new document with title name from template
        Raise exception if document already exists
        """
        self.check_for_project()
        file_extension = '.md'
        # Replace special characters in filename that make doesn't handle
        filename = title+file_extension
        filename = filename.replace(" ","_")
        filename = filename.replace("'","")
        # Raise exception if document already exists
        if os.path.exists(filename):
            raise FileExistsError(filename + ' already exists')
        config = configparser.ConfigParser()
        config.read(self.project_config)
        template = self.get_template(config, template_opt)
        bibliography_exists = os.path.exists(config['default']['bibliography'])
        rendered_template = template.render(config=config, title=title,\
                bibliography=bibliography)
        # Save render to new doc
        with open(filename, 'w') as doc:
            doc.write(rendered_template)

    def get_template(self, config, template_opt):
        """
        Return jinja_env.get_template() object
        Takes ConfigParser() object
        """
        # Get default tempalte from project settings
        default_template = config['default']['template']
        # Render template
        jinja_loader = jinja2.FileSystemLoader(self.project_template_dir)
        jinja_env = jinja2.Environment(loader=jinja_loader)
        template_file = template_opt if template_opt else default_template
        template = jinja_env.get_template(template_file)
        return template

    def make(self, output):
        """
        Use make and pandoc to generate outputs
        """
        cmd = ['make', '-f', os.path.join(self.project_dir, 'makefile'), output]
        subprocess.run(cmd, cwd=os.getcwd())

    def print_csl(self):
        """
        Print CSL files in csl dir
        """
        csl_files = self.get_csl()
        for csl in csl_files:
            print(csl)
        return csl_files

    def get_csl(self):
        """
        Return tuple of CSL files
        If in vsuite project, files are from that project
        Else, files are from global data dir
        """
        global_csl_dir = os.path.join(self.global_data_dir, 'project_files/csl')
        if self.in_project():
            csl_files = self.get_csl_from_dir(self.project_csl_dir)
        else:
            csl_files = self.get_csl_from_dir(global_csl_dir)
        return csl_files

    def get_csl_from_dir(self, csl_dir):
        """
        Return tuple of csl files in csl dir
        """
        csl_paths = glob.glob(csl_dir+'/*.csl')
        csl_files = []
        for csl_path in csl_paths:
            csl_file = os.path.relpath(csl_path, csl_dir)
            csl_files.append(csl_file)
        return tuple(csl_files)

    def in_project(self):
        """
        Returns whether or not in project
        """
        return os.path.exists(self.project_dir)

    def get_project_dir(self, cursor_dir=os.getcwd()):
        """
        Return absolute path of nearest parent dir with .vsuite directory
        """
        cursor_dir = os.path.abspath(cursor_dir)
        # If in existing project root
        in_project = os.path.exists(os.path.join(cursor_dir, '.vsuite'))
        if in_project:
            return cursor_dir
        # If in filesystem root, return none
        elif cursor_dir == '/':
            return os.getcwd()
        else:
            parent_dir = os.path.abspath(os.path.join(cursor_dir, os.pardir))
            return self.get_project_dir(parent_dir)


    def get_abspaths(self):
        """Return a dict of strings whose keys are project paths (e.g.
        self.project_csl_dir), and whose values are the absolute paths to those
        directories
        """
        abspaths = {}
        for subdir in self.relpaths_project:
            abspath = os.path.join(self.project_dir, self.relpaths_project[subdir])
            abspaths[subdir] = abspath
        return abspaths

    def get_relpaths(self):
        """
        Return a dict of strings whose keys are project paths (e.g.
        self.project_csl_dir), and whose values are the paths to those
        directories relative to the present working directory
        """
        relpaths = {}
        for subdir in self.abspaths:
            relpath = os.path.relpath(self.abspaths[subdir], os.getcwd())
            relpaths[subdir] = relpath
        return relpaths
