# Query Parameters

You can parse key value pairs out of the [URL query string](/notes/urls-query-strings.md) using `request.GET` in your view functions as input.
These are called **query parameters**.
That is a `QueryDict` which acts basically like a dictionary.

```py
# If the matching request URL was: '/user?user_name=david'
def view(request):
    params = request.GET
    params['user_name']  #> 'david'
```

Note that your [route pattern](/notes/django-routes.md) should _not try to match the query string_, the part with the question mark, just like you don't try to match the `http://` part.
Write the route pattern for just the [path part](/notes/urls-paths.md) of the URL.

Check out the [docs](https://docs.djangoproject.com/en/1.9/ref/request-response/#querydict-objects) for specifically how to use `QueryDict` objects.
You might need to lookup more [magic methods](http://rafekettler.com/magicmethods.html).

In general, use query parameters if your input is a sort of "modifier" on the path.
