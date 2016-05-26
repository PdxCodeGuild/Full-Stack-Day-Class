# Basic Git

[Git](https://git-scm.com) is a widely-used and excellent version control system.


Git calls the directory it's tracking all changes in a **repository**.

Git stores timestamped snapshots of the state of the repo called **commits**.
Each commit has a globally unique **hash**, an author, a timestamp, a description of what changed, a **parent** commit, and inside stores the exact changes made to the files from the last commit.

```
commit 6aeba8f3f2c386e4dc97fd3e0b8fbfee8d751ac5
Author: David Selassie <david@pdxcodeguild.com>
Date:   Tue Mar 29 16:29:27 2016 -0700

    Fixes bug in user input.
```

Commits build on top of each other to form a **history**, the full record of all snapshots of a project.
The most recent commit is called `HEAD`.

```
Time --->
C1 - C2 - C3 - C4
                |
                HEAD
```

Git gives you a suite of command line tools.
All commands below are run from within the repository directory.

## Making a Directory a Repo

To turn the current working directory into a Git repo and have git track all changes in it.

```bash
git init
```

This will make a secret `.git` directory.
Don't touch anything in it or delete it.
It contains the repo's history.

## Committing Changes
Committing is the process of taking changes in the working directory.

```
                   --- git add FILES... -->
Working Directory                            Index --- git commit --> HEAD of History
                  <-- git reset FILES... ---
```

### Commit Messages

If you forget to add `-m` when you commit, you might be thrown into a terminal text editor called Vim that's very confusing.
Don't panic.
Press escape.
Type `:q!`.
Press enter.

That should quit the editor and you can run `git commit` again and not forget the `-m"MESSAGE"`.

## Status

If you're ever not sure what's going on, run:
```bash
git status
```

This will give you a summary of all the files Git knows about and whether they've changed, been staged, or haven't been added in any commits yet.

## Viewing Changes

```
Working Directory <-- git diff --> Index <-- git diff --cached --> HEAD of History
                  <---------------- git diff HEAD --------------->
```

## Viewing History

```bash
git log
```

## Basic Workflow

If you're the only person working on a repo just on your computer, you can have a simple, one-way workflow.

1. Make changes using your editor to the working directory.
1. Stage those changes in the index using `git add FILES...`.
1. Commit those staged changes in the index to your local history using `git commit`.
