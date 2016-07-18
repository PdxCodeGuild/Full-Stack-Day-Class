# Git Branching Workflow

## Before Working

Make a new branch for each practice problem you work on from now on.

1.  Before you start some speculative work, make a feature branch _off of master_.
    Checkout master `git checkout master`.
    Then make a new branch `git checkout -b BRANCH`.

1.  If you ever change which problem you're working on, list the branches with `git branch` then check out the relevant one using `git checkout BRANCH` before committing.

## Working

Now repeat until work on a practice problem is done:

1. Make changes using your editor to the working directory.
1. Stage those changes in the index using `git add FILES...`.
1. Commit those staged changes to your history of the feature branch using `git commit`.
1. Push those commits to GitHub `git push` (follow printed directions if first push).

## Complete

Once you believe your solution to the problem is complete and you want to turn it in:

1. Ensure that you've pushed that problem branch to GitHub; check it out and run `git push`.
1. Make a Pull Request on GitHub for that branch into master.
1. I'll then comment on the Pull Request.

## Satisfactory Feedback

Once I email you with feedback saying your solution is Satisfactory or Distinguished:

1. Merge the Pull Request for that project on GitHub using the big green button.
1. Delete the finalized branch of GitHub using the "delete branch" button that appears after merging.
1. Go to the master branch `git checkout master`.
1. Pull the new version that GitHub just made for you `git pull`.
1. Delete the finalized feature branch from your local machine with `git branch -d BRANCH`.

## Unsatisfactory Feedback

If I email you with feedback saying your solution is Unsatisfactory and needs more work:

1. Ensure that you've checked out the branch for this problem using `git checkout BRANCH`.
1. Repeat the steps above in "Working" until the feedback has been addressed.
1. No need to make another Pull Request; if you push that branch to GitHub, the Pull Request is updated automatically.
