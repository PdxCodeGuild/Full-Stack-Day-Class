# Views

**Views** are functions that define _each page_ on your site.
They have to take a single argument, a [HTTP request object](https://docs.djangoproject.com/en/1.9/ref/request-response/#httprequest-objects), and return a [HTTP response object](https://docs.djangoproject.com/en/1.9/ref/request-response/#httpresponse-objects) with the HTML that should be rendered for that page.
They live in `views.py` in the application root.

Inside the view function, _anything_ can happen!
That's where you'll put your complex logic for figuring out what's on a page.

View functions are just _interface_ functions.
They should:

1. Take input out of the request
1. Put it in a form that the logic main wants
1. Convert the response from the logic main into a response
1. Return the response

The simplest example of a view would be:

```py
from django.http import HttpResponse

def render_page(request):
    """Renders the HTML for some random page."""
    return HttpResponse('This will be HTML.')
```
