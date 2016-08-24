# Django Debugging

Debugging Django projects are just as easy as normal Python projects.

## Print

`print` function calls still work!
They still print to the terminal.
Just make sure you hit the appropriate view that runs the code that prints.

## Shell

Django lets you run your application functions from the command line.

```bash
python manage.py shell
```

That will drop you into a Python interpreter that has access to your app.
Then you can import your app _by name_ and call all of the functions to try stuff out.

```py
>>> from DJANGO_APP_NAME import logic
>>> logic.try_something()
```

When we get to it, it's important to remember that if your function modifies the DB in your app, it will _also do so here_!
Be careful.

## Routing

Double check that your routes are correct.
Sometimes something might be broken but only because a route was forgotten or the regexp was never hit.
Overview the [routing order](/notes/django-routes.md).
