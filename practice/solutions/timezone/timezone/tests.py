"""timezone Tests.

This module has code to load doctests into the Django test framework.

All modules that contain doctests need to be manually imported and added to DOCTEST_MODULES.
If you add a new module or add sub-modules, they'll have to be added here too.
"""
import doctest

from . import logic
from . import models
from . import views


DOCTEST_MODULES = [
    logic,
    models,
    views,
]


def load_tests(loader, tests, ignore):
    """Add all known modules with doctests as unittest tests, which is what Django runs.

    This function will be called by the unittest discovery code.
    """
    for module in DOCTEST_MODULES:
        tests.addTests(doctest.DocTestSuite(module))
    return tests
