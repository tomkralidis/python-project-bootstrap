# Python Package Bootstrap

This is a template when starting Python projects.

## Spirit/Principles

- https://en.wikipedia.org/wiki/DevOps
- setUp/tearDown: https://m.subbu.org/code-the-infra-8c67a869cb89
- reproducible workflow: http://bost.ocks.org/mike/make
- versioning: https://semver.org
- virtualenv: https://virtualenv.pypi.io
- dependencies are fetched, not managed in version control
  - pip: https://pip.pypa.io/en/stable/
- platform independence, use os
- Python
  - develop modules for reuse, scripts are the last step
  - logging, not print statements
    - command line functions as [click](http://click.pocoo.org/5/) functions
    - no print statements
  - everything is callable
  - tests, tests, tests
  - PEP8: http://www.python.org/dev/peps/pep-0008/ , specifically:
    - 4 spaces, NOT tabs
    - UNIX line endings, NOT DOS
    - 4 spaces, NOT tabs
    - did we mention 4 spaces, NOT tabs?
    - always absolute imports
    - always run code through flake8 before committing:
```bash
    pip install flake8
    flake8 foo.py
```

## Overview of Structure

```
python-package-bootstrap/
|__ foopackage/  # the actual package (to be renamed)
|   |__ __init__.py  # always set `__version__` to x.y.z 
|   |__  # more code goes here
|   |__ tests/
|   |   |__ data/  # test data files (if none, you don't need this directory)
|   |   |__ run_tests.py  # unittest style testing, see https://docs.python.org/3/library/unittest.html
|__ .gitignore  # Python-based files to ignore
|__ LICENSE  # update project name, set year (YYYY)
|__ MANIFEST.in  # if there are non-python files that should be included in the distribution (see https://docs.python.org/3/distutils/sourcedist.html#specifying-the-files-to-distribute)
|__ README.md  # provide a description and items as per the headings in [Markdown](https://en.wikipedia.org/wiki/Markdown) format
|__ requirements.txt  # dependencies, see https://pip.pypa.io/en/latest/user_guide/#requirements-files
|__ requirements-dev.txt  # developer-centric dependencies (testing, packaging, etc.)
|__ setup.py  # setup script, set UPPERCASE variables scripts should be set as list

## Common workflows

```bash
# work in a virtualenv
virtualenv -p python3 myvenv
cd myvenv
. bin/activate
git clone https://github.com/tomkralidis/python-project-bootstrap.git
cd python-project-bootstrap
# run tests
cd tests && python run_tests.py
# create a distribution
python setup.py sdist  # result is in dist/foopackage-x.y.z.tar.gz
```
