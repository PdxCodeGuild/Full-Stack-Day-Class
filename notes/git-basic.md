# Basic Git

[Git](https://git-scm.com) is a widely-used and excellent version control system.

Git keeps track of _all_ of the content in a directory and changes to it.
That directory is called a **repository**.
Git _can not_ keep track of random files in random locations on your filesystem, only all files under a single directory.

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

## Installing and System Setup

## OS X

Use Homebrew to install Git.

```bash
brew install git
```

## Windows

[Download Git](https://git-scm.com/download) and install it.

Next, run this setup command to deal with [end lines](http://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/).

```bash
git config --global core.autocrlf true
```

## System Setup

Then, you need to do some initial setup and tell Git about yourself.
Fill in your real name and email.

```bash
git config --global user.name 'YOUR NAME'
git config --global user.email 'YOUR EMAIL ADDRESS'
git config --global core.editor 'atom --wait'
git config --global push.default simple
```

Then run the following commands to enable your shell prompt to display the Git branch you're on.

```bash
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh > ~/.git-prompt.sh
cat <<EOF >> ~/.bashrc
source ~/.git-prompt.sh
GIT_PS1_SHOWDIRTYSTATE=1
GIT_PS1_SHOWUNTRACKEDFILES=1
PS1='\u@\h \W$(__git_ps1 " (%s)") \\$ '
EOF
```

## Commands

Git gives you a suite of command line tools to manage this history.
All Git commands look like `git SUBCOMMAND [FILES...]`.
They are run from within the repository directory.

### Making a Directory a Repo

To turn the current working directory into a Git repo and have git track all changes in it, you have to **init** it.

```bash
git init
```

This will make a hidden `.git` directory in the repository directory.
Don't modify anything in it by hand or delete it.

**Do not turn your home directory into a Git repository.**
Git tracks _all_ changes in the repository directory, so you don't want it to have to deal with your music and cat pictures.
This is why we made a separate [portfolio directory](/notes/course-portfolio.md).

Do not turn a sub-directory of a repository into a repository.
Git allows you to do this, but it is hell.
You'll only be running `git init` twice or three times in this course.

## Committing Changes

**Committing** is the process of taking changes in the working directory.

This happens in a few stages because commits can contain multiple changes in multiple files or parts of files.

Add all of the changes you want to package up in a commit to the **index** using `git add FILES...`.
The index is like the loading dock or staging area.
To remove things from the index use `git reset FILES...`.

Once your index contains all of the changes you want, run `git commit` to package it up and clear the index for more changes.

```
                   --- git add FILES... -->
Working Directory                            Index --- git commit --> HEAD of History
                  <-- git reset FILES... ---
```

### Commit Messages

Every commit has a **commit message** which is a short description of what changes are made in the commit.

When you run `git commit`, Atom will open up and let you write out that message.
Write a summary, save the file, then _close the Atom window_.

To remind you what you are committing, there will be some commented out summary information.
Things after `#` are not saved as part of the commit.

Messages tend to be a short one line description of the change, then a blank line, then a longer list of specific changes.

## Status

If you're ever not sure what's going on, check on the **status** of the repo.

```bash
git status
```

This will give you a summary of all the files Git knows about and whether they've changed, been staged, or haven't been added in any commits yet.
Green files are going to be committed.

## Viewing Changes

To view specific line changes between your index or working directory or history use **diff** commands.

```
Working Directory <-- git diff --> Index <-- git diff --cached --> HEAD of History
                  <---------------- git diff HEAD --------------->
```

## Viewing History

To see your **history** of commits look at the **log**.
It is a reverse chronological order of all of your repository's commits.

```bash
git log
```

When you have a long history, `git log` will take control of the terminal and you can use the arrow keys to scroll up and down in your history.
Use the `q` key to quit and return to the prompt.
