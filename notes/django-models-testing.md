# Django Doctesting

You can use [doctests](/notes/doctests.md) to

```py
pip install pytest pytest-django
```

`pytest.ini`

```
[pytest]
addopts = --doctest-modules
testpaths = DJANGO_APP_NAME
DJANGO_SETTINGS_MODULE = DJANGO_APP_NAME.settings
```

`DJANGO_APP_NAME/conftest.py`

```py
"""pytest Configuration."""
import pytest


def pytest_collection_modifyitems(items):
    """Allow all tests to use the Django DB."""
    for item in items:
        item.add_marker(pytest.mark.django_db)
```
