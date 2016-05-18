# Git Remotes and GitHub
We've [already learned](/notes/git-basics.md) how to convert a local folder to a repository and record a history of all changes to it.
But source control is also about allowing others to collaborate on your code, so we need to learn how to _share_ your history with other repos.

Each local git repo can have a **remote repository**.
A remote is another computer that is keeping track of the history of commits.

You can **push** new commits you've made locally to the remote's history.
You can also **pull** new commits someone else has made remotely to your local history.

## GitHub
We'll be learning how to use GitHub as our remote repository and public display of our _class portfolio_.
This is so other people can easily browse and discover the portfolio you're building through the class.

[Sign up for GitHub](https://github.com) if you haven't already.

## Linking an Existing Local Repo to GitHub
Since we already have made your `~/codeguild` folder into a repo, we need to make a new _empty_ repo on GitHub.

Go to the [new repo page](https://github.com/new) and create a new one named `codeguild`.
_Uncheck_ the "Initialize this repository with a README" box.

We now need to **add that remote** to our local repository.
The standard "main remote" name is `origin`.
(That's because usually the remote is the origin of your source code, not the current local machine.)
```bash
git remote add origin https://github.com/GITHUBUSERNAME/codeguild.git
```
It will probably ask you for your GitHub username and password.

Great!
Let's actually push our code to origin / GitHub and save that we want to push there by default.
```bash
git push --set-upstream origin master
```
You only have to run this fancier pull command once.

## Pushing and Pulling
The commands `git push` and `git pull` are the core ones to do one-way syncing with a remote:
```
              --- git push -->
Local History                  Remote History
              <-- git pull ---
```

Run them from inside the local repo directory.

You _only_ are synchronizing _commits_.
Uncommitted changes in the working directory aren't synced.

## Basic Remote Workflow
If you're the only person working on a repo, you can have a simple, one-way workflow:
1. Make changes using your editor to the working directory.
1. Stage those changes in the index using `git add FILES...`.
1. Commit those staged changes in the index to your local history using `git commit -m"MESSAGE"`.
1. Push those new commits in your local history to the default remote history using `git push`.

## Update Your Portfolio
Now, as you progress through the class, you _must_ be periodically pushing your history to GitHub.
When I ask you to submit assignments, I'll be checking GitHub links.
