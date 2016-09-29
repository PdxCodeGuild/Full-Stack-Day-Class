#!/usr/bin/bash

set -e

if (( $# < 1 ))
then
    echo "USAGE: $0 NAME"
    echo 'Sets up an existing Django project in CWD under the dir NAME to use Heroku.'
    echo
    echo "E.g. If you have a Django app in ~/codeguild/PROJECT/PROJECT, run this script from ~/codeguild like `$0 PROJECT`."
    exit 1
fi

NAME="$1"

if [[ ! -d "$NAME" ]]
then
    echo "No project $NAME in CWD!"
    exit 2
fi

set -x

cd "$NAME"
echo 'python-3.5.1' > runtime.txt
source venv/bin/activate
pip install gunicorn whitenoise dj-database-url django-storages boto
if [[ "$OSTYPE" == darwin* ]]
then
    brew install postgresql
    LDFLAGS=-L/usr/local/opt/openssl/lib CPPFLAGS=-I/usr/local/opt/openssl/include PKG_CONFIG_PATH=/usr/local/opt/openssl/lib/pkgconfig pip install psycopg2
else [[ "$OSTYPE" == linux* ]]
then
    sudo apt-get install python3-dev
    pip install psycopg2
else
    pip install psycopg2
fi
pip freeze > requirements.txt
echo "web: gunicorn $NAME.wsgi --log-file -" > Procfile
heroku create "$NAME"
heroku addons:create heroku-postgresql:hobby-dev
heroku config:set DJANGO_SECRET_KEY=$(cat /dev/urandom | LC_CTYPE=C tr -dc '[:print:]' | tr -d "[:blank:]'\"" | head -c 50)
echo $'# Environment variables that cause local Heroku runs to contact production DB.' > .env
heroku config -s >> .env
cat <<'EOF' >> .gitignore
# Heroku production secrets
.env
EOF
cat <<'EOF' >> "$NAME/settings.py"
# Heroku production settings
# Will overwrite settings with production config vars from env variables if
# Heroku is detected.

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

if 'DJANGO_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(conn_max_age=500)

# AWS media storage
# http://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

if 'AWS_ACCESS_KEY_ID' in os.environ:
    INSTALLED_APPS.append('storages')
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
EOF
heroku local:run python manage.py migrate
heroku local:run python manage.py createsuperuser

deactivate
set +x
