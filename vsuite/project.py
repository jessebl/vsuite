import os
import subprocess
import configparser
import shutil
import jinja2
import dirsync
import glob
from .user import User
from .asset import Asset

class Project(User):
    """Represent a project directory

    The present working directory is considered to be the vsuite project root,
    unless one of its parent directories is a project, in which case that
    directory is considered to be.

    Initializing sets attributes about where various directories and project
    resources would be, if they exist.

    """

    def __init__(self, use_pwd=False):
        # self.project_path is absolute
        self.project_path = self.get_project_dir(use_pwd=use_pwd)
        self.project_dir = os.path.join(self.project_path, '.vsuite')
        self.project_config = os.path.join(self.project_dir, 'config.ini')
        self.project_csl_dir = os.path.join(self.project_dir, 'csl')
        self.project_template_dir = os.path.join(self.project_dir, 'templates')
        self.csl = Asset('csl', 'csl', 'csl', self.project_path)
        self.templates = Asset('templates', 'templates', 'j2',\
                self.project_path)
        self.bibliographies = Asset('bibliographies', '..', 'bib',\
                self.project_path)
        self.assets = [self.csl, self.templates, self.bibliographies]
        # dict of paths relative to project_dir
        self.relpaths_pwd = self.get_relpaths()
        User.__init__(self)


    def init(self):
        """Initialize project directory

        Reinitialize vsuite for the user, and initialize the present working
        directory as a project directory. This includes creating the .vsuite
        directory, creating and empty bibliography file, and initializing a git
        repo.

        """
        self.global_init()
        self.git_init()
        self.create_project_dir()
        self.create_bibliography()


    def create_bibliography(self):
        """Create bibliography if it doesn't exist

        Bibliography checked and created with ``bibliography`` value from
        project settings
        """
        config = configparser.ConfigParser()
        config.read(self.project_config)
        bibliography_name = config['default']['bibliography']
        bibliography_file = os.path.join(self.bibliographies.relpath_pwd(),\
                bibliography_name)
        if not os.path.exists(bibliography_file):
            with open(bibliography_file, 'w') as bib:
                bib.write('')

    def git_init(self):
        """Initialize git repository in project_path
        """
        cmd = ['git', 'init']
        with open(os.devnull, 'w') as fp:
            subprocess.run(cmd, cwd=self.project_path, stdout=fp)

    def create_project_dir(self):
        """Create ``.vsuite`` directory if it doesn't exist
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
        """Verify that current directory is a project

        Raises:
            (FileExistsError): If not in a project directory

        """
        if not os.path.exists(self.project_dir):
            raise FileExistsError('Not in a vsuite project')

    def create_doc(self, title, template_opt=None):
        """ Create new document with title name from template

        Args:
            title (str): Title of document, used as basis for filename
            template_opt (str): Document template to override default template
                set in project settings

        Raises:
            (FileExistsError): If file with same name already exists

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
        bibliography_path = os.path.join(self.bibliographies.relpath_pwd(),\
                config['default']['bibliography'])
        bibliography_exists = os.path.exists(bibliography_path)
        rendered_template = template.render(relpaths=self.relpaths_pwd,\
                config=config, title=title, bibliography=bibliography_exists)
        # Save render to new doc
        with open(filename, 'w') as doc:
            doc.write(rendered_template)

    def get_template(self, config, template_opt):
        """Get template object to use for new document

        Args:
            config (ConfigParser): config of project

        Returns:
            jinja2.environment.Template: template to use

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
        """Use make and pandoc to generate outputs

        Use makefile from .vsuite directory, which leverages pandoc to generate
        requested outputs

        Args:
            output (str): name of argument to pass to make

        """
        cmd = ['make', '-f', os.path.join(self.project_dir, 'makefile'), output]
        subprocess.run(cmd, cwd=os.getcwd())

    def get_project_dir(self, cursor_dir=os.getcwd(), use_pwd=False):
        """Absolute path to consider as project directory

        Use present working directory if no parent directory is a project
        directory.

        Args:
            cursor_dir (str): directory to check for project

        Returns:
            str: absolute path

        """
        if use_pwd:
            return os.getcwd()
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

    def get_relpaths(self):
        """Get paths of project resources relative to pwd

        Note:
            Mostly legacy method, preserved only using all assets' relative
            paths in ``self.create_doc()``

        Returns:
            dict: relative paths of project paths (e.g. the project's csl_dir)

        """
        relpaths = {}
        for asset in self.assets:
            relpaths[asset.name] = asset.relpath_pwd()
        return relpaths
