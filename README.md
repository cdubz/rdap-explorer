# RDAP Explorer
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**RDAP Explorer** provides a basic frontend for querying, formatting and
navigating RDAP information using:

- [IPWhois](https://github.com/secynic/ipwhois) by Philip Hane.
- [pycountry](https://bitbucket.org/flyingcircus/pycountry) by [Christian Theune](https://flyingcircus.io/)
- [JSONFormatter](http://azimi.me/json-formatter-js/) by [Mohsen Azimi](http://azimi.me/).

## Installation

### Prerequisites

- Python 3.x
- Pip3 + pipenv

### Initiate environment

```shell
pip3 install --user pipenv
cd /path/to/cloned/repo
export PIPENV_VENV_IN_PROJECT=1
pipenv install --three
```

### Configure

```shell
cd rdap_explorer/settings
cp example.py custom.py
```

Open `custom.py` in your preferred editor and add, at least, a `SECRET_KEY`.

### Run standalone

```shell
pipenv shell
export DJANGO_SETTINGS_FILE=rdap_explorer.settings.custom
python manage.py migrate
python manage.py createcachetable
python manage.py runserver
```

The application should now be available at 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/).
