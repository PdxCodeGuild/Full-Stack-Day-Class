# App Structure
From here on out, each of your practice problems and your capstone will be full fledged Python **applications**.
Each app lives in its own directory and has a few necessary parts.
```
APP_NAME/
  venv/
    ...
  requirements.txt
  .gitignore
  YOUR_SOURCE.py
  YOUR_MODULE/
    __init__.py
    MORE_YOUR_SOURCE.py
```

* `venv` should be the [virtualenv for this project](virtualenv.md#create).
* `requirements.txt` should be the output of [freezing](virtualenv.md#freeze) your virtualenv with all of the necessary packages installed.
* `.gitignore` should ignore `venv` and any other OS or editor junk like `.DS_Store` or `.cache` or `__pycache__`.
