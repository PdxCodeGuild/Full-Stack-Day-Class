# Good Code

What is good code?

* Correct
* Understandable
* Extendable
* Maintainable

A reviewer would ask themselves:

* Can I tell it correctly solves the problem?
* Does it stand on its own? Do I need the original developer to answer questions?
* Could I easily add a new feature to this code?
* Could debug this code at 3 A.M.?

If the answers are ever "no", then the reviewer finds ways to restructure the code to solve that issue.

Those are all very abstract goals.
I have taught you specific techniques and ideas that help fulfill those goals.

* Naming ensures code is understandable
* Docstrings / JSDocs ensure code is understandable
* Testable code is easy to see if correct
* Functions with explicit inputs and outputs are easy to test
* Named functions for each step are easier to understand and test
* Separating input, output, transforms, and main ensures code is extendable
* Using shared / standard libraries instead of writing your own code ensures correctness
* Following style guides rigorously ensures code reduces barriers to understanding
