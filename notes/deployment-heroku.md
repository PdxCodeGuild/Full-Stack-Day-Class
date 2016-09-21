# Heroku Deployment Steps

[Heroku](https://www.heroku.com) is a service that automates provisioning of servers and databases, setting up the server environment, installing your application code and virtualenv, running your server and database, giving it a public address, and monitoring.
Really, it does it all for a basic web app.
All you have to do is fit their configuration conventions and push your code to them with Git.

Super slicks.
Some people be hating on it.
Not sure why; possibly because it makes things too easy or because it makes things too hard if you don't fit their app model.

Let's set up things to match their configuration conventions.
All of these files need to live in the _repo root_.
If you have extra directory structure, you'll have to move things around before starting this.

If you are on macOS or Linux, I have a bash script that will perform all of the following steps for you: [django-heroku.sh](/bin/django-heroku.sh).
There is also a tutorial on the [Heroku docs](https://devcenter.heroku.com/articles/getting-started-with-python#introduction).

## 1. Runtime

Heroku looks in a file called `runtime.txt` for what kind of language environment it should set up.
Tell it to configure Python 3 by putting the following in that file.

```
python-3.5.1
```

## 2. Install Production Dependencies

We need to install some extra dependencies that will allow your Django app to run in a more robust way and connect to external databases and data stores.
Update your `requirements.txt` with the following.

```bash
pip install gunicorn whitenoise psycopg2 dj-database-url django-storages boto3
pip freeze > requirements.txt
```

* [Gunicorn](http://gunicorn.org) is a way of running your web app via multiple processes so that it can handle concurrent requests.
* [whitenoise](http://whitenoise.evans.io/en/stable/) properly implements serving static files from your Django process.
* [psycopg2](http://initd.org/psycopg/) provides a DB interface to PostgreSQL.
* [dj-database-url](https://pypi.python.org/pypi/dj-database-url) gives us a way to easily get PostgreSQL connection info.
* [django-storages](http://django-storages.readthedocs.io/en/latest/) gives an interface for storing Django user-uploaded files to S3.
* [boto3](http://boto3.readthedocs.io/en/latest/) is an AWS / S3 interface.

## 3. Procfile

Heroku looks in a `Procfile` to determine what processes to run.
In that file, put the following to get it to run your server as a web server.
Replace `DJANGO_APP_NAME` with the name of your app module.

```
web: gunicorn DJANGO_APP_NAME.wsgi --log-file -
```

This command tells Heroku to run your server through Gunicorn and write all logs to standard out.

## 4. Make Heroku App and DB

First, if you haven't before, install the [Heroku CLI Toolbelt](https://devcenter.heroku.com/articles/getting-started-with-python#set-up).
You can easily get it with Homebrew with `brew install heroku`.

Second, [sign up for a Heroku account](https://signup.heroku.com).
You'll be prompted for that email and password in some of these commands.

Now tell Heroku to make space for your app and database.
Replace `DJANGO_APP_NAME` with the name of your app.

```bash
heroku create DJANGO_APP_NAME
heroku addons:create heroku-postgresql:hobby-dev
```

Once you've created an app, all Heroku commands know about it by looking in the Git config.

## 5. Setup Production Environment

Now we need to tell Heroku about any custom environment variables it should pass to our app when it runs on Heroku.
When we created the DB, it already made a `DATABASE_URL` environment variable, but we need to make the Django secret key.
The following bash one-liner will generate a new random secret key and save it in Heroku's environment variable list.

```bash
heroku config:set DJANGO_SECRET_KEY=$(cat /dev/urandom | LC_CTYPE=C tr -dc '[:print:]' | tr -d "[:blank:]'\"" | head -c 50)
```

It will also come in handy to have a local copy of all of the production environment variables.
We'll put that in a file called `.env`.
You should also Git ignore that file so the keys aren't revealed publicly.

```bash
echo $'\n.env' >> .gitignore
heroku config -s > .env
```

## 6. Leveled App Configuration

The app's `settings.py` now needs to be configured to use those environment variables if they exist and change the DB connected to, etc.
Append my [example settings](/demos/example_heroku_settings.py) to the end of your `settings.py`.

## 7. Migrate Production DB

Now we need to setup the production DB with users and any empty tables.
Each of these commands will run `manage.py` locally, but with the configuration saved in `.env` and that will cause it to talk to the production database.

```bash
heroku local:run python manage.py migrate
heroku local:run python manage.py createsuperuser
```

**Do not use "brassmonkey" for the password!**
This user will be publicly accessible if someone finds the admin interface of your app.

## 8. Push Code to Heroku

Whenever you want Heroku to run your code, you push the branch you want running to it.
The initial setup added a `heroku` Git remote.

```bash
git push heroku master
```

This will kick off a cascade of operations that after a few minutes will have your server running!
Heroku automatically gives you a randomly generated DNS name for your service.
Heroku gives you a convenient command to open a browser pointing at the server with.

```bash
heroku open
```
