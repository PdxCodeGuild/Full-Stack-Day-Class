# Templates

If view functions respond with HTML, then the requesting browser can render it!

The obvious way to do this is clunky:

```py
from django.http import HttpResponse

def render_greeting(request):
    name = get_user_name()
    return HttpResponse('<!DOCTYPE html><html><body><h1>Hi, {}!</h1></body></html>'.format(name))
```

Instead you can use **templates**, HTML files that contain some instructions for interpolating data into them.
Then tell your view function to render the template.

If we saved this in `templates/DJANGO_APP_NAME/greet.html` in your Django application root:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Greeting</title>
  </head>
  <body>
    <{{ title_type }}>Hi, {{ name }}!</{{ title_type }}>
  </body>
</html>
```

Then our view could **render** that template and fill in all of the values.
You give each template a **context** dictionary of the variables the template needs to render.
This context is like the "arguments" for running the template as a "function".

```py
from django.shortcuts import render

def render_greeting(request):
    template_arguments = {
        'name': get_user_name(),
        'title_type': 'h2',
    }
    return render(request, 'DJANGO_APP_NAME/greet.html', template_arguments)
```

The resulting response content would be:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Greeting</title>
  </head>
  <body>
    <h2>Hi, David!</h2>
  </body>
</html>
```

Template variable names and context dictionary keys need to match.
The template doesn't know or care what Python variable names you use in the view.

**Templates have no knowledge of HTML syntax.**
They just interpolate strings.
You're writing Django template code that needs to write HTML code.

Templates live in the `templates/DJANGO_APP_NAME` directory in the Django application root.

## Basic Features

For a full list of features, read the [Django template docs](https://docs.djangoproject.com/en/1.9/ref/templates/language/).

## Variables

**Template variables** work just like Python string formatting.
Use the name of the template variable in double braces `{{}}`.
If a template variable has structure, you can reach inside the structure using a dot operator.
Nested dictionaries, classes, and lists all work.

In your view

```py
class Color:
    def __init__(self, hex_string):
        self.hex_string = hex_string

def render_template(request):
    template_arguments = {
        'model': 'Mustang',
        'facts': {
            'make': 'Ford',
            'color': Color('#FF0000'),
        },
        'years_owned': [1981, 2001],
    }
    return render(request, 'template.html', template_arguments)
```

In `template.html`:

```html
<div>
    <h2 style="color: {{ facts.color.hex_string }};">{{ model }}<small>{{ facts.make }}</small></h2>
    <span>Years Owned: {{ years_owned.1 }}, {{ years_owned.2 }}</span>
</div>
```

## Links

Django gives you a way of not having to remember your routing patterns.
Instead you should refer to other views by their [short name](/notes/django-routes.md) using the `url` tag.

In your routes:

```py
urlpatterns = [
    url(r'^comment$', views.render_comment_form, name='comment_form'),
]
```

In your template if you want to link to that route:

```html
<a href="{% url 'comment_form' %}">Post a comment.</a>
```

The resulting HTML would be:

```html
<a href="/comment">Post a comment.</a>
```

## If Tag

You can optionally output different HTML by using an `if` tag.
It has exactly the same semantics as a [normal Python if statement](/notes/py-branching-blocks.md), although it has [fewer operators it supports](https://docs.djangoproject.com/en/1.9/ref/templates/builtins/#if).

In your view:

```py
def render_template(request):
    template_arguments = {
        'message': 'You are on fire!',
        'type': 'warning',
    }
    return render(request, 'template.html', template_arguments)
```

In `template.html`:

```html
{% if type == 'warning' %}
<span class='yellow'>Warning: {{ message }}</span>
{% elif type == 'info' %}
<span class='green'>Info: {{ message }}</span>
{% else %}
<span>{{ message }}</span>
{% endif %}
```

This will only output one of the three `span`s.

## For Tag

You can repeat sections of HTML by using a `for` loop tag.
It has exactly the same semantics as a [normal Python for loop](/notes/py-for-loops.md):
the `for` tag creates a new template variable with a given name for each item in the loop.

In your view:

```py
class AddressBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

def render_template(request):
    template_arguments = {
        'friends': [
            AddressBookEntry('David', '503-555-9895'),
            AddressBookEntry('Helen', '503-555-1234'),
        ]
    }
    return render(request, 'template.html', template_arguments)
```

In `template.html`:

```html
<ul>
    {% for friend in friends %}
    <li>{{ friend.name }} - {{ friend.phone_number }}</li>
    {% endfor %}
</ul>
```

The resulting HTML would be:

```html
<ul>
    <li>David - 503-555-9895</li>
    <li>Helen - 503-555-1234</li>
</ul>
```
