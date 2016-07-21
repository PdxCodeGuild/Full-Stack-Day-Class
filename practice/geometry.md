# Practice: Geometry

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `geometry`.

Write a program that can store and manipulate rectangles and points.

Implement two value classes `Point` and `Rectangle` in modules named `point` and `rectangle` respectively.

* Points should store their `x` and `y` coordinates
* Rectangles should store their top left point, then a `w` width and `h` height
* Both should have magic repr and magic equals implemented

Then create some top-level functions in those modules that know how to operate on instances of each class.
In the `point` module:

* Find the distance between two points
* Return a new point moved by a specified amount

In the `rectangle` module:

* Know if a point is inside a rectangle
* Find the center point of a rectangle

All functions, even magic class functions, should have doctests.
