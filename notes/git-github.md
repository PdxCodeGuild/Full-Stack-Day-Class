# Git Remotes and GitHub

Each local Git repository can have a **remote**.
A remote is another computer that is also keeping track of the repository's history.

You can **push** new commits you've made locally to the remote's history.
You can also **pull** new commits someone else has made remotely to your local history.

## GitHub

We will be using [GitHub](https://github.com) as the remote for our portfolios and capstones.
[Sign up for GitHub](https://github.com/join) if you haven't yet.

## Linking an Existing Local Repo to GitHub

Since we already have made your `~/codeguild` folder into a repo, we need to make a new _empty_ repo on GitHub.

Go to the [new repo page](https://github.com/new) and create a new one named `codeguild`.
_Uncheck_ the "Initialize this repository with a README" box.

We now need to **add that remote** to our local repository.
The conventional "main remote" name is `origin`.

```bash
git remote add origin https://github.com/GITHUBUSERNAME/codeguild.git
```

It will probably ask you for your GitHub username and password.

Great!
Let's actually push our code to `origin` and save that we want to push there by default.

```bash
git push --set-upstream origin master
```

## Pushing and Pulling

**Pushing** is taking your local history and merging it with remote history.
**Pulling** is taking the remote history and merging it into your local history.

```
              --- git push -->
Local History                  Remote History
              <-- git pull ---
```

You _only_ are synchronizing commits.
Uncommitted changes in the working directory aren't synced.

GitHub has [some instructions](https://help.github.com/articles/caching-your-github-password-in-git/) you can follow to not have to type in your password every time.
