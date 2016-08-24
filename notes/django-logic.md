# MVC and Isolation

Similar to how I gave the suggestion of isolating your input, transform, and output sections of your normal Python code, there are similar suggestions for structuring your Django app.

One structural pattern is called **model-view-controller** or **MVC**.
It separates out your code into three parts named as such.

## Models

**Models** are just data container classes, with some associated serialization and storing functions.

These live in `models.py`.

## Views

**Views** are "interface" functions that define how input and output with the external world are handled.
Things like JSON serializers and deserializers, type converters, all could go here.

In general, views should not interface with models directly; they should go through a controller function.

These live in `views.py`.

## Controllers

**Controllers** are "business logic" functions.
This is where your actual application happens.

For simple applications, perhaps all of this lives in `logic.py`.
For complex applications, you might make a `logic` module and have many sub-modules.
