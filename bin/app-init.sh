#!/bin/bash

set -e

if (( $# < 1 ))
then
    echo "USAGE: $0 NAME"
    echo 'Sets up a Python project in a dir NAME in the CWD.'
    exit 1
fi

NAME="$1"

set -x

mkdir "$NAME"
cd "$NAME"
cat <<EOF > .gitignore
# Pre-parsed Python
__pycache__

# Virtualenvs
venv

# PyCharm Temporary Files
.idea
.cache

# Django Default DB
db.sqlite3

# macOS
.DS_Store
EOF
virtualenv venv
source venv/bin/activate
pip freeze > requirements.txt
