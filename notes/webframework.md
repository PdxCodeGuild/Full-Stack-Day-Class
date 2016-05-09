# Web Framework
A **web framework** is a library that does all of the piping for writing a web server for you. The most basic operation is to match URLs with code that should run and produce a response.

You can write a function for each URL in your site.
Then link them to the actual URL pattern.
Then fill in the function with whatever code is necessary to produce the HTML content.
It could talk to a DB, another web server, crunch lots of numbers, just read a file, etc.

```py
from django.conf.urls import url
from django.http import HttpResponse

urlpatterns = [
    url(r'^gallery/$', render_gallery),
]

def render_gallery(request):
    user_pictures = query_db_for_user_pictures(request.GET['user'])
    filled_template = fill_html_template_of_user_pictures(user_pictures)
    return HttpResponse(filled_template)
```
