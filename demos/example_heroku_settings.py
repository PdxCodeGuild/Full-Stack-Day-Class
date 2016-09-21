# Heroku production settings
# Will overwrite settings with production config vars from env variables if
# Heroku is detected.

MIDDLEWARE_CLASSES.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

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
