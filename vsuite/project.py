import os
import subprocess
import configparser
import shutil
import jinja2
import dirsync
from .user import User

class Project(User):

    def __init__(self):
        """
        Initialize vsuite for inheritance
        """
        self.project_path = os.getcwd()
        self.project_dir = os.path.join(self.project_path, '.vsuite')
        self.project_config = os.path.join(self.project_dir, 'config.ini')
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
        dirsync.sync(self.global_project_files, self.project_dir, 'sync', logger=dummy_logger)
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

    def create_doc(self, title):
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
        # Read template name from settings
        config = configparser.ConfigParser()
        config.read(self.project_config)
        template_dir = os.path.relpath('.vsuite/templates')
        template_file = config['default']['template']
        # Render template
        jinja_loader = jinja2.FileSystemLoader(template_dir)
        jinja_env = jinja2.Environment(loader=jinja_loader)
        template = jinja_env.get_template(template_file)
        bibliography = os.path.exists(config['default']['bibliography'])
        rendered_template = template.render(config=config, title=title,\
                bibliography=bibliography)
        # Save render to new doc
        with open(filename, 'w') as doc:
            doc.write(rendered_template)

    def make(self, output):
        """
        Use make and pandoc to generate outputs
        """
        cmd = ['make', '-f', os.path.join(self.project_dir, 'makefile'), output]
        subprocess.run(cmd, cwd=self.project_path)
