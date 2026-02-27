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
pip3 install .
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
pip3 install ".[dev]"
pip3 install ".[tests]"

pytest tests/
```


## Releasing

```bash
# create release (x.y.z is the release version)
vi pyproject.toml  # update [project]/version
git commit -am 'update release version x.y.z'
git push origin main
git tag -a x.y.z -m 'tagging release version x.y.z'
git push --tags

# upload to PyPI
rm -fr build dist *.egg-info
python3 -m build
twine upload dist/*

# publish release on GitHub (https://github.com/geopython/foopackage/releases/new)

# bump version back to dev
vi pyproject.toml  # update [project]/version
git commit -am 'back to dev'
git push origin main
```

### Conventions

* Code: [PEP 8](https://www.python.org/dev/peps/pep-0008)
* Build: [PEP 517](https://www.python.org/dev/peps/pep-0517)

### Bugs and Issues

All bugs, enhancements and issues are managed on [GitHub](https://github.com/tomkralidis/python-project-bootstrap/issues).

## Contact

* Firstname Lastname
