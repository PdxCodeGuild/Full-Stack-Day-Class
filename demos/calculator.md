# Demo: Calculator
Create a "web site" that can do simple math with positive integers.
It should be a fully formed Python and Django application.

It has two paths:
* `/plus` that adds two numbers
* `/minus` that subtracts two numbers

Each should take in two input arguments as query parameters:
* `x` first argument
* `y` second argument

Each should respond with a `200 OK` and the text of the answer.
If either input is less than zero, respond with `400 BAD REQUEST` and a message that the inputs must be positive.

[Source](/demos/calculator)

## Example
```
/plus?x=5&y=6

200 OK
11
```

```
/minus?x=5&y=6

200 OK
-1
```

```
/plus?x=5&y=-6

400 BAD REQUEST
y must be positive
```
