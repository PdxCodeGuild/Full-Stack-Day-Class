# Single Purpose Components

Similar to how I gave the suggestion of isolating your input, transform, and output sections of your normal Python code, there are similar suggestions for structuring your Django app.
When every component in your program has one purpose, it makes your code more organized, testable and composable.

## Model

The **model** is the way you are representing your business problem in code.
It includes data container classes and logic that manipulates them to do actions.

The noun classes should live in `models.py`.
If you have a ton of model classes, think about making a `models` module instead and have many sub-modules, each for one noun.

### Model Logic

As part of your model, I think you should have something called **logic**.
It contains all of the verbs and common actions you would want to perform on your

For simple applications, perhaps all of this lives in `logic.py`.
For complex applications, you might make a `logic` module and have many sub-modules.

## View

The **view** is the interface.
It is made up of "interface" functions that define how input and output with the external world are handled.

The view is a combination of templates and handler functions that work together to construct HTML.
Things like JSON serializers and deserializers, type converters, all could go here.

The handler functions live in `views.py` and the templates in `templates/DJANGO_APP_NAME/`.

## Other Architectures

[Django doesn't exactly fit a well-named architecture](https://docs.djangoproject.com/en/1.10/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names).
It has some opinions, but it doesn't require full adherence.

There are many different ways to structure your program: [model-view-controller](https://en.wikipedia.org/wiki/Model–view–controller), [model-view-adapter](https://en.wikipedia.org/wiki/Model–view–adapter), [model-view-viewmodel](https://en.wikipedia.org/wiki/Model–view–viewmodel), etc.
Each has some opinions and tradeoffs as to how verbose the code is and what kind of constraints it enables.
