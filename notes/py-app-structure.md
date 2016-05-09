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

I will call the top level `APP_NAME` directory the **repository root**.

## 1. Create Repository Root
```bash
mkdir YOUR_APP
cd YOUR_APP
```

## 2. Create Virtualenv
```bash
virtualenv venv
```

## 3. Ignore Virtualenv
```bash
echo 'venv' > .gitignore
```

## 4. Activate Virtualenv
```bash
.
```

## 4. Install Packages
```bash
pip install PACKAGE_NAME
```

## 5. Freeze Requirements
```bash
pip freeze > requirements.txt
```

## 6. Commit Initial Code

* `venv` should be the [virtualenv for this project](virtualenv.md#create).
**Do not commit your virtualenv directory!**
You should `.gitignore` this directory.
* `requirements.txt` should be the output of [freezing](virtualenv.md#freeze) your virtualenv with all of the necessary packages installed.
* `.gitignore` should ignore `venv` and any other OS or editor junk like `.DS_Store` or `.cache` or `__pycache__`.
* The rest of the files are your actual source.
