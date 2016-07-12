# Git Branching Workflow

Make a new branch for each practice problem you work on from now on.

1. Before you start some speculative work, make a feature branch using `git checkout -b BRANCH`.

Now repeat until work on a practice problem is done:

1. Make changes using your editor to the working directory.
1. Stage those changes in the index using `git add FILES...`.
1. Commit those staged changes to your history of the feature branch using `git commit`.
1. Push those commits to GitHub `git push` (follow printed directions if first push).

Once your work is done and pushed:

1. Make a Pull Request on GitHub for that branch into master.
1. I'll then comment on the Pull Request.

Once I email you with feedback and say your solution is Satisfactory or Distinguished:

1. Merge the Pull Request for that project on GitHub.
1. Go to the master branch `git checkout master`.
1. Pull the new version that GitHub just made for you `git pull`.
1. Delete the finalized feature branch from your local machine with `git branch -d BRANCH`.
1. Delete the finalized feature branch from GitHub with `git push origin --delete BRANCH`.
