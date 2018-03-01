from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vsuite',

    version='0.4.0',

    description='Plaintext project management for those who want a\
            clean and powerful workflow',

    long_description=long_description,

    url='https://git.craptops.xyz/jesse/vsuite',

    author='Jesse Bulson-Lewis',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='writing',

    packages = ['vsuite'],

    include_package_data = True,

    install_requires=['jinja2'],  # Optional

    entry_points={  # Optional
        'console_scripts': [
            'vs=vsuite.cli:main',
        ],
    },
)
