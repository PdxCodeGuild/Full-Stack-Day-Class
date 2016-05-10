# Static Files
**Static files** are files you're serving that don't change, like images, CSS, or JS, or some HTML.

Put them in `static/DJANGO_APP_NAME` in your Django application root.

Then in your templates that need to access static files at the top:
```html
{% load staticfiles %}
```

Then when you need to access their paths, use the `static` tag.
```html
<img src="{% static 'DJANGO_APP_NAME/logo.png' %}">
<link rel="stylesheet" href="{% static 'DJANGO_APP_NAME/style.css' %}">
<script src="{% static 'DJANGO_APP_NAME/main.js' %}"></script>
```

These templating tags are just forming the correct HTML.
