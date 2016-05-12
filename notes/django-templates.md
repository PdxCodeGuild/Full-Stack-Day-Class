# Templates
If view functions respond with HTML, then the requesting browser can render it!

The obvious way to do this is clunky:
```py
from django.http import HttpResponse

def render_greeting(request):
    name = request.GET['name']
    return HttpResponse('<!DOCTYPE html><html><body><h1>Hi, {}!</h1></body></html>'.format(name))
```

Instead you can use **templates**, HTML files that contain some instructions for interpolating data into them.
Then tell your view function to render the template.

If we saved this in `templates/DJANGO_APP_NAME/greet.html` in your Django application root:
```html
<!DOCTYPE html>
<html>
    <body>
        <h1>Hi, {{ name }}!</h1>
    </body>
</html>
```

Then our view could **render** that template and fill in all of the values.
You give each template a **context** dictionary of the variables the template needs to render.
```py
from django.shortcuts import render

def render_greeting(request):
    context = {'name': request.GET['name']}
    return render(request, 'DJANGO_APP_NAME/greet.html', context)
```

The resulting response content would be:
```html
<!DOCTYPE html>
<html>
    <body>
        <h1>Hi, David!</h1>
    </body>
</html>
```

Templates have no knowledge of HTML syntax.
They just interpolate strings.
You're writing Django template code that needs to write HTML code.

Templates live in the `templates/DJANGO_APP_NAME` directory in the Django application root.

## Basic Features
For a full list of features, read the [Django template docs](https://docs.djangoproject.com/en/1.9/ref/templates/language/).

## Variables
Template **variables** work just like Python string formatting.
Use the name of the variable in double braces `{{}}`.
If a variable has structure, you can reach inside the structure using a dot operator.
Nested dictionaries, classes, and lists all work.

In your view
```py
class Color:
    def __init__(self, hex_string):
        self.hex_string = hex_string

def render_template(request):
    context = {
        'model': 'Mustang'
        'facts': {
            'make': 'Ford',
            'color': Color('#FF0000'),
        },
        'years_owned': [1981, 2001],
    }
    return render(request, 'template.html', context)
```

In your `template.html`:
```html
<div>
    <h2 style="color: {{ facts.color.hex_string }};">{{ model }}<small>{{ facts.make }}</small></h2>
    <span>Years Owned: {{ years_owned.1 }}, {{ years_owned.2 }}</span>
</div>
```

## Links
Django gives you a way of not having to remember your routing patterns.
Instead you should refer to other views by their [short name](django-routes.md) using the `url` tag.

```html
<a href="{% url 'post' %}">Post a comment.</a>
```

## If Tag
You can optionally output different HTML by using an `if` tag.
It has exactly the same semantics as a [normal Python if statement](branchingblocks.md).

In your view:
```py
def render_template(request):
    context = {
        'message': 'You are on fire!',
        'type': 'warning'
    }
    return render(request, 'template.html', context)
```

In your `template.html`:
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
It has exactly the same semantics as a [normal Python for loop](forloops.md).

In your view:
```py
class AddressBookEntry:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

def render_template(request):
    context = {
        'friends': [
            AddressBookEntry('David', '507-555-9895'),
            AddressBookEntry('Helen', '507-555-1234'),
        ]
    }
    return render(request, 'template.html', context)
```

In your `template.html`:
```html
<ul>
    {% for friend in friends %}
    <li>{{ friend.name }} - {{ friend.phone_number }}</li>
    {% endfor %}
</ul>
```
