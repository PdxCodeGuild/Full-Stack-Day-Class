# Path Parameters

We've seen [query parameters](/notes/django-query-parameters.md) which are appended to the path of a URL.
You can also parse fields out of the URL path directly.
These are called **path parameters**.

In general, use path parameters if the parameter is the "subject" of the page.
Otherwise, use [query parameters](/notes/django-query-parameters.md).

If your matching path has a [named capture](/notes/regular-expressions.md#namedcaptures), the view function should take an argument of the same name.

So if in `urls.py`:

```py
url(r'^users/(?P<user_name>.+)$', views.user_detail)
```

Then in `views.py`:

```py
# If the matching request path was: 'users/david'
def user_detail(request, user_name):
    user_name  #> 'david'
```

## REST

Some folks have tried to formalize how HTTP interfaces and websites should be laid out.
One of those methods is called **REST**.
[Read up on it](http://www.restapitutorial.com/lessons/whatisrest.html) if you're interested.
