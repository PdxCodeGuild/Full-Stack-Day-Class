# Virtualenv
Different Python applications, ones you're developing or running, will have different dependencies.
A **virtualenv** is a way to isolate dependencies and swap them out quickly as we move between them.

A virtualenv is an isolated "installation" of Python and packages.
It is _just a directory_ that contains a "copy" of a Python interpreter, the standard library, an isolated set of installed packages, and some scripts to enable and disable itself.
When you **activate** a virtualenv, any commands that deal with Python or packages will only affect further commands inside the virtualenv.

## Installing
Virtualenv is also the name of the tooling to manage virtualenvs
The tooling is in a Python package.
You need to install it system-wide to be able to use it.
You should only need to run this once on your computer.
```bash
pip install virtualenv
```
(Some of you might need to run `pip3`).

Once it's installed, there are various actions you need to know.

## Create
The first action is to **create** a new, empty virtualenv.
I would recommend you use the name `venv`.
```bash
virtualenv -p python3 NAME
```
This will create a directory called `NAME` in the working directory.

**Do not commit your virtualenv directory!**
You should `.gitignore` this directory.

You should create a virtualenv for each separate project or problem you're working on that needs packages.
See [app structure](py-app-structure.md) for more info.

## Activate
Once you've created a virtualenv, you can **activate** it.
You have to run a script in the virtualenv directory.
On bash:
```bash
. NAME/bin/activate
```

On PowerShell:
```
NAME\Scripts\activate
```

Your prompt should change and show `(NAME)` at the beginning to let you know you've activated.

After you have activated a virtualenv, you **inside** of it.
Inside, all `python` and `pip` commands will use _their virtualenv versions_ and not the ones system-wide.
If you install packages, they'll be installed only the the virtualenv for later use.
If you run a script, you'll _only_ have access to the packages previously installed in the virtualenv.

## Modifying Packages
Once a virtualenv has been activated, all [Pip commands](pip.md) modify that virtualenv.

Inside the virtualenv, you shouldn't need to use `pip3` if you were before.

## Running Python
Once a virtualenv has been activated, you can use `python` to run Python code.
It will have access to all the installed packages in the virtualenv.

Inside the virtualenv, you shouldn't need to use `python3` if you were before.

## Freeze
**Freezing** is the process of taking all of the current packages and their versions and writing it out to `requirements.txt`.
This is how you save what dependencies your application has.
See [Python app requirements](py-app-requirements.md) for more info.
```bash
pip freeze > requirements.txt
```
`>` is a special shell operator that takes the output of the previous command and writes it to a file.

## Deactivate
Once you're done being in a virtualenv and want to use your system Python or enter a different virtualenv of a different project, you should **deactivate**.
A command is available only inside of the virtualenv.
```bash
deactivate
```

Your prompt should change back to normal showing you've been deactivated.

## Rebuild
To tell Pip to install all of the specific versions of packages in a requirements file:
```bash
pip install -r requirements.txt
```

You can use this to quickly fill an empty virtualenv with all of the required dependencies for an existing project.
