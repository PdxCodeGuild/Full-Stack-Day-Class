# Layout Problem Solving
Here are

## CSS is not a Constraint Solver
Don't expect you to be able to specify widths and heights on everything.
CSS is _not a constraint solver_.

Although one day you might have [constraint based CSS](http://gridstylesheets.org/guides/ccss/).

## Slice up Width, Sum up Height
Remember that the that core dimensions of block elements are calculated as:
* Width is top-down -- the full width of the parent element
* Height is bottom-up -- whatever is necessary to contain the children

This means that you should think about your layout _width first_.
From the _top down_, specify widths.

Then, once all of the widths are correct, work on adding or subtracting height from the _bottom up_.
_Don't_ specify heights on top or mid-level elements.
Instead, have the browser sum up the correct heights for you.

E.g.

## Be Reductionist
All of the same problem solving techniques from Python still apply here.
Work from the top-down and work on stages of your layout problem.
