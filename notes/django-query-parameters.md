# Query Parameters
You can parse key value pairs out of the [URL query string](urls.md#querystrings) using `request.GET` in your view functions as input.
These are called **query parameters**.
That is a `QueryDict` which acts basically like a dictionary.
```py
# If the matching request URL was: '/user?user_name=david'
def view(request):
    params = request.GET
    params['user_name']  #> 'david'
```

Check out the [docs](https://docs.djangoproject.com/en/1.9/ref/request-response/#querydict-objects) for specifically how to use `QueryDict` objects.
You might need to lookup more [magic methods](http://rafekettler.com/magicmethods.html).
