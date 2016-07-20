# Practice: Geometry

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `geometry`.

Write a program that can store and manipulate rectangles and points.

Implement two value classes `Point` and `Rectangle` in modules named `point` and `rectangle` respectively.

* Points should store their `x` and `y` coordinates
* Rectangles should store their top left point, then a `w` width and `h` height
* Both should have magic repr and magic equals implemented

Then, in a `main.py`, write create functions that allow the following operations on those class instances:

* Find the distance between two points
* Know if a point is inside a rectangle
* Find the center point of a rectangle
* Return a new point moved by a specified amount

All functions, even class functions, should have doctests.
