# Git Ignore
A **Git ignore** file is a list of file names for Git to ignore and not track.
It lives in a file named `.gitignore` in your repository.
It will "protect" all directories that are siblings of or are underneath where it is.

Each line in the file is a pattern to match.
You can use `#` comments.

```sh
*.txt  # Ignore all files ending in .txt
notes  # Ignore all files or directories named notes anywhere
/root_notes  # Ignore a file named "root_notes" in just the repository root
```

Here is an [example Git ignore](../demos/example_gitignore) you can copy and use.
