# Practice: Caesar Cipher

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `caesar`.
Your HTML file should be named `index.html` and your JS file named `site.js` in that directory.

A **Caesar cipher** is a way of encrypting simple text using a single number as a **key**.
Each letter is "rotated" forward by that key number.
[Read up more on it](http://www.cs.trincoll.edu/~crypto/historical/caesar.html).

* Implement a function `caesarEncrypt(plainStr, key)` that returns the encrypted version.
* Implement a function `caesarDecrypt(encStr, key)` that returns the plain text version.

## Advanced

Write a function `guessKey(encStr)` that uses letter frequency analysis to guess which key is correct.
[That same page](http://www.cs.trincoll.edu/~crypto/historical/caesar.html) has a technique for deciding which key is "closest".
Use the algorithm there as a guideline, but try to adapt it to the principles and structural ideas we've learned in the class.
