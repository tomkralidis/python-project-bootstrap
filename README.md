# foopackage

## Overview

This is the foopackage package.

## Installation

The easiest way to install foopackage is via the Python [pip](https://pip.pypa.io)
utility:

```bash
pip3 install foopackage
```

### Requirements
- Python 3
- [virtualenv](https://virtualenv.pypa.io)

### Dependencies
Dependencies are listed in [requirements.txt](requirements.txt). Dependencies
are automatically installed during foopackage installation.

### Installing foopackage

```bash
# setup virtualenv
python3 -m venv --system-site-packages foopackage
cd foopackage
source bin/activate

# clone codebase and install
git clone https://github.com/geopython/foopackage.git
cd foopackage
python3 setup.py build
python3 setup.py install
```

## Running

```bash
cp foopackage-config.env local.env
vi local.env # update environment variables accordingly

foopackage --version
```

### Using the API

```python
# Python API examples go here
```

## Development

### Running Tests

```bash
# install dev requirements
pip3 install -r requirements-dev.txt

# run tests like this:
python3 foopackage/tests/run_tests.py

# or this:
python3 setup.py test

# measure code coverage
coverage run --source=foopackage -m unittest foopackage.tests.run_tests
coverage report -m
```

## Releasing

```bash
rm -fr build dist *.egg-info
python3 setup.py sdist bdist_wheel --universal
twine upload dist/*
```

### Code Conventions

* [PEP8](https://www.python.org/dev/peps/pep-0008)

### Bugs and Issues

All bugs, enhancements and issues are managed on [GitHub](https://github.com/tomkralidis/python-project-bootstrap/issues).

## Contact

* Firstname Lastname
