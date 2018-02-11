import os
import subprocess
import configparser
import shutil
import jinja2
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
        if not os.path.exists(self.project_dir):
            shutil.copytree(self.global_project_files, self.project_dir)
            self.init_project_config()
        else:
            raise FileExistsError('Project already initialized')

    def init_project_config(self):
        """
        Copy user config into project
        """
        config = configparser.ConfigParser()
        config.read(self.global_config_file)
        with open(self.project_config, 'w') as configfile:
            config.write(configfile)

    def create_doc(self, title):
        """
        Create new document with title name from template
        Raise exception if document already exists
        """
        file_extension = '.md'
        filename = title+file_extension
        # Raise exception if document already exists
        if os.path.exists(filename):
            raise FileExistsError(filename + ' already exists')
        # Read template name from settings
        config = configparser.ConfigParser()
        config.read(self.project_config)
        template_file = config['default']['template']
        # Render template
        jinja_loader = jinja2.FileSystemLoader('.vsuite')
        jinja_env = jinja2.Environment(loader=jinja_loader)
        template = jinja_env.get_template(template_file)
        rendered_template = template.render(config=config, title=title)
        # Save render to new doc
        with open(filename, 'w') as doc:
            doc.write(rendered_template)
