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

The top level `PROJECT_NAME` directory is the **project root**.

If you are on macOS or Linux, I have a bash script that will perform all of the following steps for you: [app-init.sh](/bin/app-init.sh).

## 1. Create Project Root

For each of your problems, create a new project root directory with the name of your project.

```bash
mkdir PROJECT_NAME
cd PROJECT_NAME
```

## 2. Setup Git Ignore

Then setup a [Git ignore](/notes/git-ignore.md) file so you won't commit your virtualenv.
**Don't commit your virtualenv!**

Save [this example file](/demos/example_gitignore) in `.gitignore` in your project root.

If this project is part of your portfolio repo, it's okay that there's an inner `.gitignore`: they just union.

## 3. Create Virtualenv

[Create a new virtualenv](/notes/py-virtualenv.md#create) in your repository root.

## 4. Activate Virtualenv

[Activate that virtualenv](/notes/py-virtualenv.md#activate) that you just made.

## 4. Install Packages

[Install](/notes/py-pip.md#install) all of the dependent packages you'll need.

## 5. Freeze Requirements

[Freeze](/notes/py-virtualenv.md#freeze) your initial dependency versions.
If you ever install more dependencies, you'll have to re-freeze.

## 6. Commit Initial Code

Commit all these files (other than the `venv` directory).
