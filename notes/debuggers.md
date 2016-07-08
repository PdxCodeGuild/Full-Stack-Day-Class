# Debuggers

Until now, we've been print debugging.
Variables contain invisible values until you print them out.

Print debugging is hard because you have to:

1. Explicitly put in print statements
1. Visualize what order the program is running in to know which print is in what order
1. Re-run the program whenever to check on new data

**Debuggers** solve these problems.
They allow you to pause or break execution on a specific line of code, called a **breakpoint**, and inspect all of the variables in the current scope with their current values.
They also can break execution whenever an exception is thrown, so you can check on the values of variables without needing to re-run the program.

Use the green "bug run" button in [PyCharm](/notes/pycharm.md) to run your script, stopping at breakpoints.
