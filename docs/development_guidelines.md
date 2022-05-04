Some principles and guidance for SANCdpd development
====================================================

# General principles

## Relationship between application code and the database

The SANCdpd software cannot run without the SANCdpd database.  However, the two
should be kept separate.  The software code can depend on the database
structure, but should never assume any particular values are stored in the
database tables.



# Resources explaining the rationale for various design choices


## Project structure

The following resources were consulted in structuring the Python code for SANCdpd:

- Python Package Structure
    - https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6
    - https://web.archive.org/web/20220421034438/https://dev.to/codemouse92/dead-simple-python-project-structure-and-imports-38c6

- Real Python:  Python Application Layouts
    - https://realpython.com/python-application-layouts/
    - https://web.archive.org/web/20220421034601/https://realpython.com/python-application-layouts/

- Away With Ideas: The optimal python project structure
    - https://awaywithideas.com/the-optimal-python-project-structure/
    - https://web.archive.org/web/20220421034838/https://awaywithideas.com/the-optimal-python-project-structure/


## Global cross-module configuration variables

SANCdpd includes a module called conf.py for sharing configuration information across modules.

See explanation here:
https://docs.python.org/3/faq/programming.html#how-do-i-share-global-variables-across-modules



# General resources for the tools used to write SANCdpd software


## Coding standards

- Official Python Style Guide ("PEP 8")
    - https://peps.python.org/pep-0008/

- Python docstrings
    - Use docstrings to document Python Code.  This is a very good thing to do!
    - https://peps.python.org/pep-0257/

- SQL quotation marks
    - SQLite is lenient about quotation marks.  However, it is best to follow the SQL standard.  String literals should be enclosed by single quotes.  Column names in double quotes (when necessary).  The MySQL convention of using backticks (`grave`) quotes is discouraged.


## General Python resources

- How to Think Like a Computer Scientist
  (Good general introduction to Python programming.)
    - https://runestone.academy/ns/books/published/thinkcspy/index.html

- Official Python programming FAQ
  (Excellent list of Python-specific questions and pitfalls.)
    - https://docs.python.org/3/faq/programming.html

- Official Python 3 documentation
    - https://docs.python.org/3/


## General SQLite resources

- SQLite Tutorial
  (Thorough, clear, and comprehesive guidance on SQLite's flavor of SQL.)
    - https://www.sqlitetutorial.net/

- Official SQLite Documentation
    - https://www.sqlite.org/docs.html
