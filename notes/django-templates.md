# Templates
If view functions respond with HTML, then the requesting browser can render it!

The obvious way to do this is clunky:
```py
from django.http import HttpResponse

def render_greeting(request):
    name = request.GET['name']
    return HttpResponse('<!DOCTYPE html><html><body><h1>Hi, {}!</body></html>'.format(name))
```

Instead you can use **templates**, HTML files that contain some instructions for interpolating data into them.
Then tell your view function to render the template.

If we saved this in `templates/greet.html` in the application root:
```html
<!DOCTYPE html>
<html>
    <body>
        <h1>Hi, {{ name }}!</h1>
    </body>
</html>
```

Then our view could **render** that template and fill in all of the values.
You give each template a **context** dictionary;
it contains just the variables the template needs to render.
```py
from django.shortcuts import render

def render_greeting(request):
    context = {'name': request.GET['name']}
    return render(request, 'greet.html', context)
```

Templates should live in a `templates` directory in the application root.

## Basic Features
For a full list of features, read the [Django template docs](https://docs.djangoproject.com/en/1.9/ref/templates/language/).

## Variables
Template **variables** work just like Python string formatting.

```html

```

## If Tag

```html

```

## For Tag

```html

```
