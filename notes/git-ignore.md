# Git Ignore

A **Git ignore** file is a list of file names for Git to ignore and not track.
You want to tell Git to not worry about tracking files that are not your source, things like derived data, caches, etc.

It lives in a file named `.gitignore` in your repository.
It will "protect" all directories that are siblings of or are underneath where it is.

Each line in the file is a pattern to match.
You can use `#` comments.

```sh
*.txt  # Ignore all files ending in .txt
notes  # Ignore all files or directories named notes anywhere
/root_notes  # Ignore a file named "root_notes" in just the repository root
```

The Python interpreter generates `__pycache__` directories which contain pre-parsed code.
They should not be committed, since they are derived from your actual source and might change.
Add it to your Git ignore.

```sh
__pycache__
```

Here is an [example Git ignore](/demos/example_gitignore) you should copy and use in your portfolio repo.
