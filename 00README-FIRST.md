# Python Package Bootstrap

This is a template when starting Python projects.

## Spirit/Principles

- https://en.wikipedia.org/wiki/DevOps
- https://m.subbu.org/code-the-infra-8c67a869cb89
- reproducible workflow: http://bost.ocks.org/mike/make
- versioning: https://semver.org
- virtualenv: https://virtualenv.pypi.io
- dependencies are fetched, not managed in version control
  - pip: https://pip.pypa.io/en/stable/
- platform independence, use os
- Python
  - develop modules for reuse, scripts are the last step
  - logging, not print statements
    - command line functions as [click](https://click.palletsprojects.com/en/stable) functions
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
    pip3 install flake8
    flake8 foo.py
```

## Overview of Structure

```
|____LICENSE  # update project name, set year (YYYY)
|____pyproject.toml  # project configuration, dependencies, version
|____tests  # pytest setup
| |____util.py  # utilities only for testing
| |______init__.py  # module
| |____test_foopackage.py  # sample test runner (can have more)
| |____data  # test data files (if none, you don't need this directory)
|____README.md # provide a description and items as per the headings in [Markdown](https://en.wikipedia.org/wiki/Markdown) format
|____foopackage  # the actual package (to be renamed)
| |______init__.py
|____.gitignore  # files to ignore in version control
```


## Common workflows

```bash
# work in a virtualenv
virtualenv -p python3 myvenv
cd myvenv
. bin/activate
git clone https://github.com/tomkralidis/python-project-bootstrap.git
cd python-project-bootstrap
# run tests
pytest tests/
# create a distribution
python3 -m build  # result is in dist/foopackage-x.y.z.tar.gz
```
