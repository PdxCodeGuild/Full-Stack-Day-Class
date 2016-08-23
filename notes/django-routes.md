# Routes

**Routing** is specifying the mapping from a URL path pattern to a specific view function.
This is done by pairing together [regular expressions](/notes/regular-expressions.md) matching the _just_ the [path](/notes/urls-paths.md) of a URL to a view function with `django.conf.urls.url`.
These parings have to live in `urls.py` in the application route in a list named `urlpatterns`.
Give each of your routes a **short name**, which are used to refer to the pages they render in code later.

So a simple `urls.py` would be:

```py
from django.conf.urls import url

# Import your views module, so you can tell Django about the view functions.
from . import views

urlpatterns = [
    # Link together path regexps with view functions imported from views
    # module.
    # Give each view a name.
    url(r'^$', views.index, name='index'),
    url(r'^posts$', views.posts, name='posts'),
]
```

Every path should start with `^` and end with `$` to ensure you don't over-match.
In general, paths should not try to match a trailing slash `/`, e.g. `^posts$` is better than `^posts/$`.

Routes are evaluated _in order_.
Whatever the first route to match is the one used.
Think about having all of your routes unique.

```py
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^base', views.base),  # If you forget a $, will "eat" longer paths.
    url(r'^base/(?P<named>.+)$', views.base_capture),  # Captures might "eat" longer paths.
    url(r'^base/wont_match$', views.base_wont_match),  # Will never match because of _both_ of above routes.
]
```

Read up in the [Django docs about the url function](https://docs.djangoproject.com/en/1.9/ref/urls/#django.conf.urls.url).
