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
echo $'venv\n__pycache__\n\n.DS_Store' > .gitignore
virtualenv venv
. venv/bin/activate
pip install django
pip freeze > requirements.txt
django-admin startproject "$NAME" .
perl -i -pe "s/^(INSTALLED_APPS = \[)/\1\n    '$NAME',/g" "$NAME/settings.py"
echo $'\ndb.sqlite3' >> .gitignore
echo $'STATIC_ROOT = os.path.join(BASE_DIR, \'staticfiles\')' >> "$NAME/settings.py"
echo $'\nstaticfiles' >> .gitignore
echo $'\nMEDIA_URL = \'/media/\'\nMEDIA_ROOT = os.path.join(BASE_DIR, \'mediafiles\')' >> "$NAME/settings.py"
echo $'\nmediafiles' >> .gitignore
mkdir -p "mediafiles"
echo "\"\"\"$NAME Views.\"\"\"" > "$NAME/views.py"
echo "\"\"\"$NAME Models.\"\"\"" > "$NAME/models.py"
echo "\"\"\"$NAME Logic.\"\"\"" > "$NAME/logic.py"
echo "\"\"\"$NAME Admin Configuration.\"\"\"" > "$NAME/admin.py"
mkdir -p "$NAME/templates/$NAME"
mkdir -p "$NAME/static/$NAME"
python manage.py migrate

deactivate
set +x
