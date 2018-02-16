Quick Start
-----------

You might want to check out [this
demo](https://asciinema.org/a/0P06UgeiTM6EL4R8jbYdz7D7j) for an example of the
steps in this quick start.

Initialize a project with ``vs init``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

vsuite uses the concept of a project directory, in which you have
various vsuite docs (which are simple pandoc markdown files) accompanied
by a hidden ``.vsuite`` directory that holds accompanying files like
`CSL files <https://en.wikipedia.org/wiki/Citation_Style_Language>`__
and document templates. To get started using it, you need to initialize
a directory as a vsuite directory:

.. code:: bash


    vs init

This effectively creates an empty bibliography file, initializes a git
repository, and creates the ``.vsuite`` directory which includes a
project config file.

Create a new markdown document with ``vs new``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, you can get started with actually creating markdown files using
vsuite:

.. code:: bash


    vs new <document title>

This will create a file ``<document title>.md``, after dropping or
modifying spaces or some special characters (since GNU make really
struggles with these things…). This file is generated from a template by
vsuite and includes a YAML header that specifies fields for pandoc. This
file is the one that you are meant to edit and do your work in. Tuning
your text editor for use with markdown will be greatly helpful in this,
since the whole point of this writing paradigm is to leave you, the
writer, with more time doing actual writing. (For example, see `this vim
configuration
file <https://github.com/jessebl/installscripts/blob/master/configs/vim-writer/.writer.vimrc>`__.)

Render your document with ``vs make``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you’re ready to turn your markdown source into files for use by
others:

.. code:: bash


    vs make <project name>.<file extension of desired format>

    # E.g generate a PDF of your document file "best_document.md"

    vs make best_document.pdf

This uses GNU make along with a makefile in ``.vsuite`` to freshly
generate the specified file unless it has been updated more recently
than the source markdown file. Hence, you can always make sure that you
have up-to-date documentation with ``vs make``. The currently available
formats are:

-  pdf

-  odt

-  docx
