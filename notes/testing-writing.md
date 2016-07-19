# Writing Good Tests

What kind of tests should you write?
What should you assert?

* Each test should assert _one specific requirement or type of output_ of each function.
* If there are multiple requirements, have multiple tests for a single function.
* A rule of thumb: one test per "branch" or "or".
* Assert as broadly as possible; check all of the output.

Testing and the code are synergistic.
**If code is hard to test, it's not good code.**
Often times that means the way the problem is being broken up isn't the best.
