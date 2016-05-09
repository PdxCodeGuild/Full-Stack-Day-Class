# Routes
**Routing** is specifying the mapping from a URL path pattern to a specific view function.
This is done by pairing together [regular expressions](regular-expressions.md) matching the _path_ of a URL to a view function with `django.conf.urls.url`.
These parings have to live in `urls.py` in the application route in a list named `urlpatterns`.

So a simple `urls.py` would be:
```py
from django.conf.urls import url

# Import your views module, so you can tell Django about the view functions.
from . import views

urlpatterns = [
    # Link together path regexps with view functions imported from views
    # module.
    url(r'^$', views.index),
    url(r'^posts/$', views.posts),
]
```

Read up in the [Django docs about the url function](https://docs.djangoproject.com/en/1.9/ref/urls/#django.conf.urls.url).
