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

```html
<!DOCTYPE html>
<html>
    <body>
        <h1>Hi, David!</h1>
    </body>
</html>
```

Templates live in the `templates/DJANGO_APP_NAME` directory in the Django application root.

## Basic Features
For a full list of features, read the [Django template docs](https://docs.djangoproject.com/en/1.9/ref/templates/language/).

## Variables
Template **variables** work just like Python string formatting.
Use the name of the variable in

```py
album_entry = {
    'description': 'Cool pic of cats',
    'src_url': 'htttp://aksdjflaksdjf.gif'
}

render(request, 'temp.html', {'album_entry': album_entry})
```

```html
<div>
    <span>{{ album_entry.description }}</span>
    <img src="{{ album_entry.src_url }}">
    <{{ tag_name }}> </{{ tag_name }}>
</div>
```

## If Tag

```py
context = {
    'message': 'You are on fire!',
    'type': 'warning'
}
render(request, 'temp.html', context)
```

```html
{% if type == 'warning' %}
<span class='yellow'>Warn: {{ message }}</span>
{% elif type == 'info' %}
<span class='green'>Info: {{ message }}</span>
{% endif %}
```

## For Tag
```py
context = {
    'messages': [
        'Neat',
        'fine',
        'hairy'
    ]
}
render(request, 'temp.html', context)
```

```html
<ul>
{% for message in messages %}
<li>{{ message }}</li>
{% endfor %}
</ul>
```
