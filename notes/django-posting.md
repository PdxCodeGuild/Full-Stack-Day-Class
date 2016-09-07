# Posting Forms

Getting input from the user via forms is a two-page process.

1. Display a form.
1. Display an acknowledgement of success or error.

Use POST if the data change is persistent!

**Form submission** uses the default behavior of HTML forms.
If you specify the `action` attribute and give it a path, when the submit event happens, the browser will create a HTTP POST request with all of the data in the form.
It will then perform that POST request and _load_ the response as a _new page_.

If your form HTML looks like:

```html
<form action="{% url 'image_submit' %}" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="text" name="title">
    <input type="file" name="image">
    <input type="submit">
</form>
```

If you don't specify `enctype="multipart/form-data"`, then the file data will not be sent to the server.

Then you can receive the form data via a route named `image_submit`:

```py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^image_form$', views.render_form, name='image_form'),
    url(r'^image_form/submit$', views.render_submit, name='image_submit'),
]
```

And in your view, access the named data via the `request.POST` dictionary.
Files, since they might be giant, are loaded via a separate `request.FILES` dictionary.

```py
from . import models

def render_submit(request):
    title = request.POST['title']  # String in the name "title"
    image = request.FILES['image']  # Content as a file-like object

    models.save_image(image, title)

    return HttpResponse('We got your submission!')
```
