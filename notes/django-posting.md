# Posting Data
There are two ways to get data back from the user to the server: form submission and AJAX posting.

## Form Submission
**Form submission** uses the default behavior of HTML forms.
If you specify the `action` attribute and give it a path, when the submit event happens, the browser will create a HTTP POST request with all of the data in the form.
It will then perform that POST request and _load_ the response as a _new page_.
```html
<h2>Submit an Image</h2>
<form action="submit.html" method="post">
    <input type="text" name="title">
    <input type="file" name="image">
    <input type="submit">
</form>
```

```py
from . import logic

def render_submit(request):
    title = request.POST['title']  # String in the name "title"
    image = request.FILES['image']  # Content as a file-like object
    logic.save_image(image, title)
    return HttpResponse('We got your submission!')
```

## AJAX
1. Overwrite submit event handler
1. Prepare your data
1. Manually submit
1. Have a callback that updates the page.
```js
function submitImage() {
    var formData = $('form').serialize();
    $.post('submit.html', formData, function(data) {
        $('.message').text(data);
    });
}
```

The same Python code would process it.
