# Django Problem Solving

When starting a Django problem from scratch, use the following steps to get started.

## 1. Make Application

Follow [the steps to make a Python application](/notes/py-app-structure.md).
[Install](/notes/py-pip.md) the Django package in your virtualenv.

## 2. Init Django Files

Follow the steps to initialize a [Django project](/notes/django-init.md).
Commit all the resulting files.

## 3. Route

[Create routes](/notes/django-routes.md) for each page or data endpoint you'll need.

## 4. Write Views

[Create view functions](/notes/django-views.md) for each page that return some simple test data.

## 5. Test Routes / Views

[Run your server locally](/notes/django-serving-locally.md) and see if you can get the views to load.

## 6. Write Models

Think about what nouns your program is going to need and write [model classes](/notes/django-models.md) for each.

## 7. Write Logic

Work on your [core program logic component](/notes/django-components.md) in modules that don't use Django.

## 8. Test Logic

Use the [Django shell](/notes/django-shell.md) and doctests to ensure that your logic is functioning correctly.

## 9. Link Logic

Now call your logic functions from your view functions.
Add in any type conversion or serialization that handles converting between the textual format of the request / response and the native data types of your logic.

## 10. Test Application

Now in your browser, see if the views work!
