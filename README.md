# vsuite

vsuite is a project management suite for UNIX-like OSes aimed at writers who
want tools that help--rather than hinder--them in their writing. At its core,
it is essentially a command-line wrapper around existing tools to simplify the
task of using them to create markdown source files. Writing in markdown allows
the writer, once she is up-to-speed on its usage, to separate the
conceptually-distinct tasks of writing and typesetting, in a manner largely
inspired by [this](http://ricardo.ecn.wfu.edu/~cottrell/wp.html)
[essay](https://web.archive.org/web/*/http://ricardo.ecn.wfu.edu/~cottrell/wp.html).
Take a look at the workflow in the quickstart guide to see if you might benefit
from using this software.

**Note:** vsuite is considered to be in early alpha, and as such should not be
considered reliable yet. With that said, since it is a wrapper and never puts
itself in charge of deleting or overwriting any user data, the risk of using it
should be very minimal. It should also go without saying, but you should always
backup any data that matters.

## Installation

### Install required software

- pandoc (for rendering markdown to other formats)

- pandoc-citeproc (for citations in markdown)

- git (for optional versioning)

- make (for simplifying rendering of markdown)

- pip3 (for installing vsuite)

For Ubuntu 16.04:

```bash

sudo apt install pandoc pandoc-citeproc git make python3-pip

```

For Fedora 27:

```bash

sudo dnf install pandoc pandoc-citeproc git make python3-pip

```

### Install vsuite

Install vsuite as a Python package using pip3 pointed to this repo:

```bash

pip3 install --user git+<URL of this repo>

```

The program will place files in `~/.local/share/vsuite` and store its config in
`~/.config/vsuite`. The requisite files should be placed when the program is
run, but this has not yet been tested to any rigorous degree. Pip also creates
a vsuite executable named `vs` at `~/.local/bin/vs`, but if that location is
not not a part of your PATH, you will need to manually add it.

## Quick Start

For more detailed documentation, check the wiki as it evolves.

vsuite uses the concept of project directory, in which you have various vsuite
docs (which are simple [pandoc
markdown](https://rmarkdown.rstudio.com/authoring_pandoc_markdown.html) files)
accompanied by a hidden `.vsuite` directory that holds accompanying files like
[CSL files](https://en.wikipedia.org/wiki/Citation_Style_Language) and document
templates. To get started using it, you need to initialize a directory as
a vsuite directory:

```bash

vs init

```

This effectively creates an empty bibliography files, initializes a git
repository, and creates the `.vsuite` directory, including a project config
file.

Finally, you can get started with actually creating markdown files using
vsuite:

```bash

vs new <document title>

```

This will create a file `<document title>.md`, with spaces replaced by
underscores (since GNU make can't handle spaces...). This file is generated
from a template by vsuite, includes a YAML header that specifies fields for
pandoc. This file is the one that you are meant to edit and do your work in.
Tuning your text editor for use with markdown will be greatly helpful in this,
and is where most productivity gains will be found.

When you're ready to turn your markdown source into files for use by others:

```bash

vs make <project name>.<file extension of desired format>

# E.g generate a PDF of your document file "best_document.md"

vs make best_document.pdf

```

This uses `make` along with a makefile in `.vsuite` to freshly generate the
specified file unless it has been updated more recently than the source
markdown file. Hence, you can always make sure that you have up-to-date
documentation with `vs make`. The currently available formats are:

- pdf

- odt

- docx

Adding other formats that pandoc supports is just a trivial addition to the
[makefile](vsuite/project_files/makefile). If you find yourself using a format
that isn't included yet, please submit a pull request!

# CSL licenses

The [csl files](vsuite/project_files/csl) here are licensed with their
respective licenses by their respective copyright owners, noted within the files themselves.
