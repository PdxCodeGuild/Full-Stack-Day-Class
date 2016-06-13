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
echo "from django.contrib.auth.models import User as U; if not U.objects.get(name='admin'): U.objects.create_superuser('admin', 'admin@localhost', 'brassmonkey')" | python manage.py shell
python manage.py runserver
deactivate

set +e
