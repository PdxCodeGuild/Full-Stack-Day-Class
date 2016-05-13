# Posting Forms
Getting input from the user via forms is a two-page process.
1. Display a form.
1. Display an acknowledgement of success or error.

Only use POST if the data change is persistent!

**Form submission** uses the default behavior of HTML forms.
If you specify the `action` attribute and give it a path, when the submit event happens, the browser will create a HTTP POST request with all of the data in the form.
It will then perform that POST request and _load_ the response as a _new page_.
```html
<form action="{% url 'image_submit' %}" method="post">
    {% csrf_token %}
    <input type="text" name="title">
    <input type="file" name="image">
    <input type="submit">
</form>
```

```py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/$', views.render_submit, name='image_submit')
]
```

```py
from . import logic

def render_submit(request):
    title = request.POST['title']  # String in the name "title"
    image = request.FILES['image']  # Content as a file-like object
    logic.save_image(image, title)
    return HttpResponse('We got your submission!')
```
