# Demo: Git Remotes

```
~/portfolio $ git remote add origin https://github.com/selassid/portfolio.git
~/portfolio $ git remote -v
origin	https://github.com/selassid/portfolio.git (fetch)
origin	https://github.com/selassid/portfolio.git (push)
~/portfolio $ git push --set-upstream origin master
Counting objects: 6, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (3/3), done.
Writing objects: 100% (6/6), 516 bytes | 0 bytes/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/selassid/portfolio.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
~/portfolio $ atom book.txt
~/portfolio $ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   book.txt

no changes added to commit (use "git add" and/or "git commit -a")
~/portfolio $ git add book.txt
~/portfolio $ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   book.txt

~/portfolio $ git commit
[master 3680ba1] Realistic book summary.
 1 file changed, 1 insertion(+), 1 deletion(-)
~/portfolio(master) % git push
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (1/1), done.
Writing objects: 100% (3/3), 301 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/selassid/portfolio.git
   e193696..3680ba1  master -> master
```
