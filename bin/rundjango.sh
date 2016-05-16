#!/bin/bash

set -e

if [[ ! -d venv ]]
then
    virtualenv venv
fi
. venv/bin/activate
if [[ "$(pip freeze)" != "$(cat requirements.txt)" ]]
then
    pip install -r requirements.txt
fi
python manage.py runserver
deactivate
