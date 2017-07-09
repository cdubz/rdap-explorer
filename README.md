# RDAP Explorer

**RDAP Explorer** provides a basic frontend for querying, formatting and
navigating RDAP information using:

- [IPWhois](https://github.com/secynic/ipwhois) by Philip Hane.
- [pycountry](https://bitbucket.org/flyingcircus/pycountry) by [Christian Theune](https://flyingcircus.io/)
- [JSONFormatter](http://azimi.me/json-formatter-js/) by [Mohsen Azimi](http://azimi.me/).

## Installation

### Prerequisites

- Python 3.x
- Virtualenv

### Initiate environment

```commandline
cd /path/to/cloned/repo
virtualenv --python=python3 .env
source .env/bin/activate
pip install -r requirements.txt
```

### Configure

```commandline
cd rdap_explorer/settings
cp example.py custom.py
```

Open `custom.py` in your preferred editor and add, at least, a `SECRET_KEY`.

### Run standalone

```commandline
python manage.py migrate --settings=rdap_explorer.settings.custom
python manage.py createcachetable --settings=rdap_explorer.settings.custom
python manage.py runserver --settings=rdap_explorer.settings.custom
```

The application should not be available at 
[http://127.0.0.1:8000/](http://127.0.0.1:8000/).