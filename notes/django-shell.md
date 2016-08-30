# Shell and Backend

Django lets you run your application functions from the command line called the **Django shell**.

```bash
python manage.py shell
```

That will drop you into a Python interpreter that has access to your app.
Then you can import your app _by name_ and call all of the functions to try stuff out.

```py
>>> from DJANGO_APP_NAME import logic
>>> logic.try_something()
```

It will also let you query for model objects and change them.

```py
>>> from DJANGO_APP_NAME import models
>>> models.Book.all()
```

Remember, if you modify any models in the shell, it modifies them permanently in the DB!
So those changes will appear in the server app when you run it!
Be careful.

## Backend Scripts

You can also write scripts that programmatically use your Django models or logic functions.
You can use them to load data into your DB or clean things up.

To do that, they need to setup Django:

```py
import django


django.setup()

...
```

Then when you run them, you have to set an environment variable that tells Django where to get the DB settings from.

```bash
DJANGO_SETTINGS_MODULE='DJANGO_APP_NAME.settings' python BACKEND_SCRIPT.py
```
