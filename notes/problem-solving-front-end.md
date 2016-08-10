# Front-End Problem Solving

First, read back through [Python advanced problem solving notes](/notes/problem-solving-adv.md).

## Actions

Think about the _top level_ actions you want to happen on your page.
E.g. "add a todo list item", "delete a tile", etc.

For each action, break it up into the following six steps and write functions to tackle each step.
It's fine if steps repeat across actions.
No function should handle more than one of these areas.

Look through the [todo demo](/demos/todo.md) to see these annotated out.
As you're working, [debug](/notes/debugging-js.md) each of your steps aggressively.

### 1. Input

Get input from the user and return it.

You'll need to use jQuery here to get info off of the page.

### 2. Transform

Perform any data transformations.
These functions should take explicit input and return the transformed data.

Don't use jQuery here.
You should already have all your data in abstract structures in variables.

### 3. Create

Create any new elements, fully set them up, then return them.

You'll need to use jQuery here to create new elements.
If new elements need to respond to events, you must register handlers here.

### 4. Modify and Synchronize

Modify the existing page.
Update properties or append new elements made in the previous step.

Remember to fully _synchronize_ the state of the page.
Figure out all the possible states the page could be in, then ensure that your modification functions can result in all of them.

You'll need to use jQuery here to modify the existing page.

### 5. Main

String together the input, transform, create, and modify steps for one action into a single function that take no arguments.
Use intermediate variables to pipe all of the data and elements around inside the main function.

Don't use jQuery here.

Each main function should just perform _one action_.

#### "Split" Actions

Realize when your "action" is actually a _set_ of actions.
E.g. a "delete an item from the list" action is actually one action for each item!
This is usually the case when you want to attach an event handler to a newly created item.

In this case, it's okay for your main function to take an argument which is the element to work on.

When you register the event handler, form a closure over the parameter.

### 6. Register

_After_ you've written functions for every other section, then worry about events.
Tell the browser to run your main functions when it sees the correct events on _existing_ elements.

Remember, this registration code is _only for initial elements_.
This code gets run with the JS is parsed, elements that are added later won't be selected and won't have event handlers added.
Add those in the "create" functions.

## Separate Style and Behavior

Avoid putting raw CSS or visual style in your JS.
Put it in classes that you swap on and off.

Have your JS "read" the HTML to figure out what to do.
Don't hard code amounts.
