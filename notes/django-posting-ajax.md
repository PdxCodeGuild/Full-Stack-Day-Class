# AJAX Posting

You can turn any parts of your logic into your own HTTP API.
Then you can have all sorts of cool interactivity, really anything you can program in Python, in your app's interface via jQuery and AJAX.

There are a few moving parts you'll need to make that work.

## Ensure Response Data is JSON Representable

Create a private view function that converts any model objects you want to respond with to a [JSON-encodable](/notes/json.md) dict.
If your model is already dictionaries, or if you're just responding with generic data, then that's fine.

```py
class Comment:
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
It should return a JSON serializable object in `django.http.JsonResponse(json_obj)`.

As a way to distinguish it from the other routes, maybe call it `return_SOMETHING` rather than `render_SOMETHING`.

```py
from django.http import JsonResponse

from . import logic


def return_comment(request, comment_id):
    """JSON endpoint which returns a specific comment by ID."""
    comment = logic.get_comment_by_id(comment_id)
    comment_json = _json_encode_comment(comment)
    return JsonResponse(comment_json)
```

## Include AJAX CSRF Setup

If any of your AJAX calls will be POSTs, put the [jQuery AJAX Django CSRF setup script](/demos/ajax_csrf_setup.js) in your project's static files folder.
Include it in the HTML just before your JS.

This ensures that jQuery will include the CSRF token in any `$.ajax()` POSTs.

```html
<script src="{% static 'DJANGO_APP_NAME/ajax_csrf_setup.js' %}"></script>
<script src="{% static 'DJANGO_APP_NAME/main.js' %}"></script>
```

## Prepare a Form / Template In Routes

Now we need some way of having the JS know what is the route to the JSON endpoint.
You can template in the route path in a few places in the HTML.
The alternative would be to template strings into the JS, which is a bit mindbending.

If you are submitting data out of a form, you can set it up like normal.
Set its action to the JSON view.
We will override the default action in the JS.

```html
<form action="{% url 'JSON_VIEW_NAME' %}" method="post">
    <textarea name="some-text"></textarea>
    <input type="submit">
</form>
```

If your JS has to make requests that don't fit into the context of a form, you can template in your routes and other data via HTML attributes on any element.
If you're using attributes just to store data, prefix them with `data-` and you can use `.data()` on an element set to get it back out.

```html
<a href="{% url 'JSON_VIEW_NAME' %}">Update current page</a>
<body data-url="{% url 'JSON_VIEW_NAME' %}"></body>
```

Then in your JS, you can access that data:

```js
$('a').attr('href');
$('body').data('url');
```

## JS AJAX Main

Write a "main" function in your site's JS that will generate any data to submit and kick off a async POST request.

If your data to the server is coming from a form, use `.serialize()` to get the data entered.
If it's not from a form, you can construct an object literal to send the data.
Then use `$.ajax()` to actually kick off the request.

You can pluck out the destination URL and method from the form itself, so it acts the most like the usual form.

```js
var sourceForm = $('#my-form');

/**
 * Returns a promise containing the JSON object for submitting the form.
 */
function submitForm() {
  var actionURL = sourceForm.attr('action');
  var submitMethod = sourceForm.attr('method');
  // This takes the data from the form and packages it up for sending.
  var formData = sourceForm.serialize();
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  }));
}
```

If the data does not come from a form, you can prepare it "manually", like you did with the other public APIs you've used.

```js
/**
 * Returns a promise containing the JSON object for submitting the form.
 */
function submitData() {
  var jsonEndpointURL = body.data('json-url');
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: jsonEndpointURL,
    method: 'post',
    data: {
      someArbiraryKeys: 'values'
    }
  }));
}
```
