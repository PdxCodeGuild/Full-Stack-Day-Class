# Front-End Problem Solving
First, read back through [Python advanced problem solving notes](adv_problem_solving.md).

Think about the _top level_ actions you want to happen on your page.
E.g. "add a todo list item", "delete a tile", etc.

For each action, break it up into the following six steps and write functions to tackle each step.
It's fine if steps repeat across actions.
No function should handle more than one of these areas.

Look through the [todo demo](../demos/todo.md) to see these annotated out.
As you're working, [debug](js_debugging.md) each of your steps aggressively.

## 1. Input
Get input from the user and return it.

You'll need to use jQuery here to get info off of the page.

## 2. Transform
Perform any data transformations.
These functions should take explicit input and return the transformed data.

Don't use jQuery here.
You should already have all your data in abstract structures in variables.

## 3. Create
Create any new elements, fully set them up, then return them.

You'll need to use jQuery here to create new elements.
You are allowed to attach event handlers to these new elements in order to set them up.

## 4. Modify
Modify the existing page.
Update properties or append new elements made in the previous step.

You'll need to use jQuery here to modify the existing page.

## 5. Main
String together the input, transform, create, and modify steps for one action into a single function that usually take no arguments.
Use intermediate variables to pipe all of the data and elements around inside the main function.

Each main function should just perform _one action_.

## 6. Register
_After_ you've written functions for every other section, then worry about events.
Tell the browser to run your main functions when it sees the correct events on the correct elements.

You should _not have any event handling_ in any of the previous steps, other than event handler registration on new elements.
