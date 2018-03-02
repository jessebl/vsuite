Why vsuite (and why not a word processor)?
==========================================

The case for content versus presentation
----------------------------------------

If you're asking this question, you probably use a `WYSIWYG
<https://en.wikipedia.org/wiki/WYSIWYG>`_ editor like Microsoft Word or
LibreOffice Writer for most of your writing needs. While there are certainly
use-cases where such programs are good tools for the job, there are also plenty
of use-cases where they aren't. `This essay
<http://ricardo.ecn.wfu.edu/~cottrell/wp.html>`_ provides a great analysis of
the failings of word processors, and this core point is largely the driving
force behind the creation of vsuite:

     Preparing printable text using a word processor effectively forces you to
     conflate two tasks that are conceptually distinct and that, to ensure that
     people's time is used most effectively and that the final communication is
     most effective, ought also to be kept practically distinct. The two tasks
     are
     
     1. The composition of the text itself...

     2. The typesetting of the document...the way in which structural elements
        will be visually represented...

     The author of a text should, at least in the first instance, concentrate
     entirely on the first of these sets of tasks. That is the author's
     business...

     I am suggesting, therefore, that should be two distinct "moments" in the
     production of a printed text using a computer. First one types one's text
     and gets its logical structure right, indicating this structure in the
     text via simple annotations...Then one "hands over" one's text to
     a typesetting program...

     -- Allin Cottrell - Word Processors: Stupid and Inefficient

The message is that **authors of text should focus on content instead of the
text's presentation**. Focusing in this way allows one to focus on one thing at
a time and more effectively use one's own mental resources. Essentially, allow
yourself as an author to not become distracted by presentation at the expense
of content, which includes the text itself along with its logical structure.

Word processors are not designed around the paradigm of separating content from
presentation. If you find yourself able to achieve separation of the two in
a word processor by tweaking your existing workflow, more power to you. It
seems likely, however, that you will still spend lots of time wrestling with
your word processor to get it to do what you want (although you're probably
used to such fights at this point).

Focusing on content
-------------------

If we writers were to focus on the text and its raw words themselves, our
writing would less clearly expose its own logical structure and then the
job of the author would be only partially completed. However, we can
indicate logical structure with only the slightest bit of effort using
a "markup language" which is used to mark up raw text with symbols that
denote logical elements (e.g. section headings). `Markdown
<https://rmarkdown.rstudio.com/lesson-8.html>`_ is an especially simple
markup language that should serve many writers well.

We now need to know how we will concretely:

1. Author markdown text

   This will be done with a text editor of your choice.

2. Turn that markdown text into a presentable piece (e.g. a nice-looking PDF)

   This will be done with Pandoc, a tool that translates various text
   formats into each other.

However, using a text editor to create markdown documents (including their
headers) from scratch and running Pandoc manually to create final
documents has two problems: the new tools might be overwhelming to those
just leaving the world of word processors, and there is a lot of
repetition in creating new documents that can be eliminated.

Using vsuite to simplify writing in markdown
--------------------------------------------

vsuite aims to generally ease the process of moving from nothing to
a finished document, exposing the functionality of the underlying tools
through a unified interface. It simplifies the initial creation of
markdown files and finished documents, and also provides a structure for
keeping track of bibliographical information.
