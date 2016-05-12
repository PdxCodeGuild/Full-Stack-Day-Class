#!/bin/bash

set -e

if (( $# < 1 ))
then
    echo "USAGE: $0 NAME"
    echo 'Sets up a Python Django project in a dir NAME in the CWD.'
    exit 1
fi

NAME="$1"

set -x

mkdir "$NAME"
cd "$NAME"
echo $'venv\n__pycache__' > .gitignore
virtualenv venv
. venv/bin/activate
pip install django
pip freeze > requirements.txt
django-admin startproject "$NAME" .
perl -i -pe "s/^(INSTALLED_APPS = \[)/\1\n    '$NAME',/g" "$NAME/settings.py"
echo $'\ndb.sqlite3' >> .gitignore
python manage.py migrate
touch "$NAME/views.py"
mkdir -p "$NAME/templates/$NAME"
mkdir -p "$NAME/static/$NAME"
deactivate

set +x
