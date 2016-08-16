# CR Guidelines

Here are some guidelines for how to approach CR and what to look for.

## Attitude

CR is not meant to be adversarial.
Everyone is working together to produce excellently crafted code.
Try to explain your own thinking and put yourself in the shoes of the other dev.

> Assume everyone is attractive, intelligent, and well-meaning.

There is no perfect decision.
Consider and debate the tradeoffs associated with each decision.

If the code does look good, no need to hunt for comments.
Let it breeze through!

[This readme](https://github.com/thoughtbot/guides/tree/master/code-review) has an excellent overview of the right kind of attitude.
Exercise [optimistic feedback](https://github.com/raganwald/presentations/blob/master/optimism.md).

## Checklists

What should you be looking for as a reviewer?

* Does it appear to be correct?
* Does it have tests if applicable?
* Do the tests show it works?
* Is the program broken up into named functions?
* Do the parts isolate steps so you know each is working? (Input, transform, output, main, style vs structure vs behavior, etc.)
* Are the functions named in a way that helps understanding?
* Are the variables named in a way that helps understanding?
* Are comments and docstrings there?
* Does any code repeat itself?
* Are there existing libraries that are re-implemented?
* Are use of error-prone patterns minimized? (index arithmetic, loops vs comprehensions, mutability, etc.)
* Are patterns codified not written out by hand?
* Are all style guides followed?

Check out these checklists for more ideas:

* [Code Review Best Practices](https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html)
* [Code Review Checklist Example](http://blog.fogcreek.com/increase-defect-detection-with-our-code-review-checklist-example/)

## Revisions

Coding and feedback are inherently iterative.
It's totally okay that your first submission to CR isn't perfect.

A draft solution can be submitted to code review for someone to check over structure, problem solving ideas, or other high-level ideas.
It's okay that it might not have proper style or docstrings everywhere, etc.

On the flip-side, as a reviewer, comment on which bits of feedback are very important or not important, or just speculative ideas.

**But, that code should not be shipped.**
Iterate and clarify your code during review.
Then only once it's done is it merged.

Code is only in `master` once it's "good".
