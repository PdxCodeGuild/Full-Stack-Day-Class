# App Structure
Each of your practice problems and your capstone should be a separate full-fledged Python **application**.
Each app lives in its own directory and has a few necessary parts.
```
PROJECT_NAME/
    venv/
    requirements.txt
    .gitignore
    YOUR_SOURCE.py
    YOUR_MODULE/
        __init__.py
        MORE_YOUR_SOURCE.py
```

The top level `PROJECT` directory is the **project root**.

## 1. Create Project Root
For each of your problems, create a new project root directory with the name of your project.
```bash
mkdir PROJECT_NAME
cd PROJECT_NAME
```

## 2. Setup Git Ignore
Then setup a Git ignore file so you won't commit your virtualenv.
**Don't commit your virtualenv!**

```bash
echo venv __pycache__ > .gitignore
```
or save [this example file](../demos/example_gitignore).

## 3. Create Virtualenv
[Create a new virtualenv](virtualenv.md#create) in your repository root.

## 4. Activate Virtualenv
[Activate that virtualenv](virtualenv.md#activate) that you just made.

## 4. Install Packages
[Install](pip.md#install) all of the dependent packages you'll need.

## 5. Freeze Requirements
[Freeze](virtualenv.md#freeze) your initial dependency versions.
If you ever install more dependencies, you'll have to re-freeze.

## 6. Commit Initial Code
Commit all these files (other than the `venv` directory).
