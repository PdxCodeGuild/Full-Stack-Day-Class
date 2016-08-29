# AJAX Posting

There are a few moving parts you'll need to make that work.

## Ensure Data is JSON Representable

Create a private view function that converts any model objects you want to respond with to a [JSON-encodable](/notes/json.md) dict.
If your model is already dictionaries, or if you're just responding with generic data, then that's fine.

```py
def Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author


def _json_encode_comment(comment):
    return {'text': comment.text, 'author': comment.author}
```

## JSON Endpoint

Create a JSON endpoint route and view.

It can take in POST or GET data if it is parameterized.
It can do stuff with the input data; e.g. save to the DB, process it, etc.
It should return a JSON serializable object with `django.http.JsonResponse(json_obj)`.

As a way to distinguish it from the other routes, maybe call it `return_SOMETHING` rather than `render_SOMETHING`.

```py
from django.http import JsonResponse


def return_comment_ack(request):
    return JsonResponse()
```

## Include AJAX CSRF Setup

If any of your AJAX calls will be POSTs, put the [jQuery AJAX Django CSRF setup script](/demos/ajax_csrf_setup.js) in your project's static files folder.
Include it in the HTML just before your JS.

This ensures that jQuery will include the CSRF token in any `$.ajax()` POSTs.

```html
<script src="{% static 'DJANGO_APP_NAME/ajax_csrf_setup.js' %}"></script>
<script src="{% static 'DJANGO_APP_NAME/main.js' %}"></script>
```

## Prepare a Form

If you are submitting data out of a form, you can set it up like normal.
Set its action to the JSON view.
We will override the default action in the JS.

```html
<form action="{% url 'JSON_VIEW_NAME' %}" method="post">
    <textarea name="some-text"></textarea>
    <input type="submit">
</form>
```

## JS AJAX Main

Write a "main" function in your site's JS that will generate any data to submit and kick off a async POST request.

If your data to the server is coming from a form, use `.serialize()` to get the data entered.
Then use `$.ajax()` to actually kick off the request.

You can pluck out the destination URL and method from the form itself, so it acts the most like the usual form.

```js
var sourceForm = $('#my-form');

function runSubmitAndUpdate() {
  var actionURL = sourceForm.attr('action');
  var submitMethod = sourceForm.attr('method');
  var formData = sourceForm.serialize();
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  }));
}
```
