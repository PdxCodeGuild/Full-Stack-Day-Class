# Path Parameters

You can parse fields out of the URL path directly.
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

Remember, named captures often introduce a lot of flexibility in the matched path, so be aware of them [eating up your longer routes](/notes/django-routes.md).
