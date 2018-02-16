# vsuite

vsuite is a project management suite for Linux OSes aimed at writers who want
tools that help--rather than hinder--them in their writing. At its core, it is
a wrapper around various technologies that makes it easy to do your writing in
[markdown](https://rmarkdown.rstudio.com/lesson-8.html) files that can easily
be turned into finished final documents. Writing in markdown allows the writer,
once she is up-to-speed on its usage, to separate the conceptually-distinct
tasks of writing and typesetting in a manner largely inspired by
[this](http://ricardo.ecn.wfu.edu/~cottrell/wp.html)
[essay](https://web.archive.org/web/*/http://ricardo.ecn.wfu.edu/~cottrell/wp.html).
Take a look at the following workflow diagram, [this
demo](https://asciinema.org/a/162560), and the [quick start
guide](http://vsuite.readthedocs.io/en/latest/quickstart.html) to try to gauge
if this software and its workflow might help you.

![workflowdiagram](docs/assets/workflow_diagram.png)

**Note:** vsuite is considered to be in early alpha, and as such should not be
considered reliable yet. With that said, since it is a wrapper and never puts
itself in charge of deleting or overwriting any user data, the risk of using it
should be very minimal. Furthermore, it should go without saying that you
should always backup any data that matters.

- [Installation](http://vsuite.readthedocs.io/en/latest/installation.html)

- [Quick Start](http://vsuite.readthedocs.io/en/latest/quickstart.html)

- [Full documentation](http://vsuite.readthedocs.io) [![Documentation Status](http://readthedocs.org/projects/vsuite/badge/?version=latest)](http://vsuite.readthedocs.io/en/latest/?badge=latest)

# CSL licenses

The [CSL files](vsuite/project_files/csl) here are licensed with their
respective licenses by their respective copyright owners, noted within the
files themselves.

You can find many, many more citation styles in [this
repo](https://github.com/citation-style-language/styles) if vsuite does not
include one that you need or want. Just place them in `.vsuite/csl` for use
within a single project, or in `~/.local/share/vsuite/project_files/csl` for
general use (and consult the wiki on how to tune your settings for new
documents!).
