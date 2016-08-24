# Static Files

**Static files** are files you're serving that don't change.
Most images, CSS, or JS on your site isn't changing, so it can be served statically.

Instead of writing a boring view function for each of these static assets, Django will automatically serve them for you.
Put them in `static/DJANGO_APP_NAME` in your Django application root.

Then, when you need to access their paths in other HTML, use the `static` templating tag.

```html
{% load staticfiles %}
<img src="{% static 'DJANGO_APP_NAME/logo.png' %}">
<link rel="stylesheet" href="{% static 'DJANGO_APP_NAME/style.css' %}">
<script src="{% static 'DJANGO_APP_NAME/main.js' %}"></script>
```

You should use the `static` tag rather then specifying the path manually because the path in your source doesn't necessarily match up with the path in your served website.
Django will figure out the served path for you.

At the top of every template that uses static tags, you need `{% load staticfiles %}`.
