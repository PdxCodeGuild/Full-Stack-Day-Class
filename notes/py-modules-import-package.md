# Package Relative Importing

We've thus far learned about [working directory relative importing](/notes/py-modules-create.md).
That only works when you are in control of what working directory you know your code will be run from.
When you're writing a package that someone else is using, that is not the case.
Then, you need to use **package-relative importing**.

This is the situation when you're writing a Django application.
Your Django application is treated as a formal Python package.
Django is running your code.
You're not running your code.

Let's say your code has the following directory structure.

```
YOUR_PACKAGE_OR_DJANGO_APP/
    models.py
    logic/
        __init__.py
        scoring.py
        gameplay.py
    views.py
```

The `YOUR_PACKAGE_OR_DJANGO_APP` directory is the root of your package and has to start the input path.
It is represented as dot `.` in package-relative imports.
That feels like the use of dot `.` in filesystem paths.

_All_ imports in your package must be relative to that root.

Within `views.py` you can import `models.py` via

```py
from . import models
```

Within `views.py` you can import `gameplay.py` via

```py
from .logic import gameplay
```

Within `gameplay.py` you can import `scoring.py` via

```py
from .logic import scoring
```

Note that is still the whole package path.
