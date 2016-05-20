#!/bin/bash

if [[ "$1" == '-h' || "$1" == '--help' ]]
then
    echo "USAGE: $0"
    echo 'Runs a Django project in the current folder.'
    echo 'Needs requirements.txt and saved migrations.'
    exit 1
fi

set -e

if [[ ! -d venv ]]
then
    virtualenv venv
fi
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
deactivate
