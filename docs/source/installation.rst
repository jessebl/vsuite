Installation
============

For the time being, vsuite is only distributed through its git repositories,
and so should be installed with pip after installing a few software
dependencies.

Required software
-----------------

-  ``pandoc`` (for rendering markdown to other formats)

-  ``pandoc-citeproc`` (for citations in markdown)

-  ``git`` (for optional versioning)

-  ``make`` (for simplifying rendering of markdown)

-  ``pip3`` (for installing vsuite)

Ubuntu 16.04
~~~~~~~~~~~~

.. code:: bash


    sudo apt install pandoc pandoc-citeproc git make python3-pip

Fedora 27
~~~~~~~~~

.. code:: bash


    sudo dnf install pandoc pandoc-citeproc git make python3-pip

vsuite
------

Install vsuite as a Python package using pip3 pointed at its git repository:

.. code:: bash


    pip3 install --user git+<URL of this repo>
    # For example, using the GitHub repo
    pip3 install --user git+https://github.com/jessebl/vsuite

The program will place files in ``~/.local/share/vsuite`` and store its
config in ``~/.config/vsuite``. The requisite files should be placed
when the program is run, but this has not yet been tested to any
rigorous degree. Pip also creates a vsuite executable named ``vs`` at
``~/.local/bin/vs``, but if that location is not not a part of your
PATH, you will need to `manually add
it <http://linuxg.net/how-to-set-a-new-path-in-bash-ksh-and-zsh/>`__.

