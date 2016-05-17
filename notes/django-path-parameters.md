# Path Parameters

We've seen [query parameters](django-query-parameters.md) which are appended to the path of a URL.
You can also parse fields out of the URL path directly.
These are called **path parameters**.

If your matching path has a [named capture](regular-expressions.md#namedcaptures) `user_name`.

```py
url(r'^users/(?P<user_name>.+)$', views.user_detail)
```

Then the view function should take in an argument named `user_name`.

```py
# If the matching request path was: 'users/david'
def user_detail(request, user_name):
    user_name  #> 'david'
```

In general, use path parameters if the parameter is the "subject" of the page.
Otherwise, use [query parameters](django-query-parameters.md).
