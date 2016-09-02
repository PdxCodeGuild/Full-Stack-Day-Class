"""pytest Configuration."""
import pytest


def pytest_collection_modifyitems(items):
    """Allow all tests to use the Django DB."""
    for item in items:
        item.add_marker(pytest.mark.django_db)
