#!/bin/sh
export FLASK_APP=./espresso/routes.py
source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0