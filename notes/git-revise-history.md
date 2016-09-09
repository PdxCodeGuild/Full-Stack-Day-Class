# Git Revisionist History

Here are some recipes for fixing common Git mistakes.

All of these recipes _modify history_.
Thus if you have already pushed to GitHub any commits that are changing, followup pushes will be rejected.
You will need to `git push -f` to overwrite those changes.
**Double check before force pushing / anything.**

## Forgot a change or file

1.  Initial history.
    ```
    A---B---C BRANCH
    ```

1.  Make changes in working directory.

1.  `git add CHANGED_FILES...` to stage those files.

1.  `git commit --amend` will re-prompt for a message then modify the most recent commit.
    ```
    A---B---C' BRANCH
    ```

## Change commit message

1.  Initial history.
    ```
    A---B---C BRANCH
    ```

1.  `git commit --amend` will re-prompt for a message then modify the most recent commit.
    ```
    A---B---C' BRANCH
    ```

## Committed changes on wrong branch, but right branch does not exist yet

1.  `git checkout WRONG_BRANCH` to use the wrong branch as the basis for the correct branch.
    Initial history.
    ```
    A---B---X---Y WRONG_BRANCH
    ```

1.  `git checkout -b RIGHT_BRANCH` to mark all commits as part of the right branch.
    ```
    A---B---X---Y WRONG_BRANCH, RIGHT_BRANCH
    ```

1.  `git reset --hard LAST_WRONG_COMMIT` makes the wrong branch what it should be.
    ```
          X---Y RIGHT_BRANCH
         /
    A---B WRONG_BRANCH
    ```

The wrong branch can be `master`.

## Committed changes on wrong branch, but right branch exists

1.  Commit changes to all files that already exist in the right branch.

1.  Initial history.
    Call the most recent commit on the wrong branch that should remain on the wrong branch the **old wrong head**.
    In this example `B` is the old wrong head.
    ```
          U---V RIGHT_BRANCH
         /
    A---B---W---X WRONG_BRANCH
    ```

1.  `git rebase --onto RIGHT_BRANCH OLD_WRONG_HEAD WRONG_BRANCH` moves just the most recent commits to the right branch.
    ```
                W---X WRONG_BRANCH
               /
          U---V RIGHT_BRANCH
         /
    A---B
    ```

1.  `git checkout RIGHT_BRANCH` checks out the right branch so we can change it.
    ```
                W---X WRONG_BRANCH
               /
          U---V RIGHT_BRANCH
         /
    A---B
    ```

1.  `git reset --hard WRONG_BRANCH` makes the right branch what it should be.
    ```
          U---V---W---X WRONG_BRANCH, RIGHT_BRANCH
         /
    A---B
    ```

1.  `git checkout WRONG_BRANCH` checks out the wrong branch so we can change it.
    ```
          U---V---W---X WRONG_BRANCH, RIGHT_BRANCH
         /
    A---B
    ```

1.  `git reset --hard OLD_WRONG_HEAD` makes the wrong branch what it should be.
    ```
          U---V---W---X RIGHT_BRANCH
         /
    A---B WRONG_BRANCH
    ```

The wrong branch can be `master`.

## Undo a merge / remove any commits

1.  Initial history.
    In a single branch's history figure out which is the **first** and **last** commits to remove.
    In this example `N` is the first and `M` is the last.
    ```
          X---Y FEATURE
         /     \
    A---B---N---M---D BRANCH
    ```

1.  `git rebase --onto FIRST^ LAST BRANCH` to splice any commits after the removed ones onto the ones before.
    ```
          X---Y FEATURE
         /
    A---B---C---D TRUNK
    ```

If any of the post-merge commits edit files introduced in the merge, the rebase will fail.

## Split a single commit into multiple ones

1.  `git checkout BRANCH` to checkout the branch with the **commit to split**.
    Initial history.
    In this example, `B` is the commit to split.
    ```
    A---B---C---D BRANCH
    ```

1.  `git rebase -i COMMIT_TO_SPLIT^`
    Mark the commit to split as needing "editing".
    Save and close the rebase todo file.
    ```
    A---B---C---D BRANCH
    ```

1.  `git reset HEAD^` to unstage all of the changes.
    ```
    A---B HEAD
         \
          C---D BRANCH
    ```

1.  Now repeat the following steps until you've created all of the commits you care about.

    1. `git add SOME_FILES...` to add just the files you want in the revised commit.

    1. `git commit` to actually make the commit.
        ```
        A---B'1---B'2 HEAD
         \
          B---C---D BRANCH
        ```

1.  `git rebase --continue` to splice in those new commits and rewrite the rest of history.
    ```
    A---B'1---B'2---C---D BRANCH
    ```

Note that if this commit is in multiple branches, you'll have to rebase all of the other branches that contain it, since you haven't changed their branch pointers.

## Filter unwanted files

Git does give you the ability to permanently remove files from all of history.
Only do this if a file is actually breaking Git:

* Giant binary file
* Committed virtualenv
* Security keys

If you're just refactoring or moving files, or even undoing or removing functionality, **don't use this feature**.
Instead revert or just move files.
Git handles moving source very gracefully.

1.  Remove a path from all commits in all branches:

    ```bash
    git filter-branch \
    --index-filter "git rm --cached -f --ignore-unmatch PATH" \
    --prune-empty \
    -- --all
    ```

1.  Ensure that things look good.
    Double check your program and tests run and that no other files are missing.

1.  `git for-each-ref --format="%(refname)" refs/original/ | xargs -n 1 git update-ref -d` will then erase the backup branches created in case things went wrong.
