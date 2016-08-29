# Query Parameters

Views that use a GET request to just respond with data can be parameterized with **query parameters** out of the [URL query string](/notes/urls-query-strings.md).

```
GET /search?queries=snuggies
```

To provide an interface for making this query, you can use a form with the `get` method.

```html
<form action="{% url 'search' %}" method="get">
    <input type="text" name="query">
    <input type="submit">
</form>
```

You can parse key value pairs out of the query parameters using `request.GET` dictionary in your view functions.
That is a `QueryDict` which acts basically like a dictionary.

```py
# If the matching request URL was: '/search?query=snuggies'
def render_search_results(request):
    request.GET['query']  #> 'snuggies'
```

Note that your [route pattern](/notes/django-routes.md) should _not try to match the query string_, the part with the question mark, just like you don't try to match the `http://` part.
Write the route pattern for just the [path part](/notes/urls-paths.md) of the URL.

```py
url(r'^search$', views.render_search_results, name='render_search_results')
```

Check out the [docs](https://docs.djangoproject.com/en/1.9/ref/request-response/#querydict-objects) for specifically how to use `QueryDict` objects.
They are different than normal dicts, as they can have multiple values.
You might need to read up on [magic methods](http://rafekettler.com/magicmethods.html) to understand their definition.
