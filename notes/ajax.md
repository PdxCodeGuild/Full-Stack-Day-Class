# AJAX

**AJAX** stands for Asynchronous Javascript And XML.
Few use XML anymore, but it has become the name for the general class of technique of updating your _current page_ with _new data from the server_ via Javascript.

There are a few moving parts you'll need to make that work.

## 1. JSON Endpoint

Create a JSON endpoint route and view.
It should take in POST data and return a `django.http.JsonResponse(json_obj)`.
It can also do stuff with the input data; e.g. save to the DB, process it, etc.
As a way to distinguish it from the other routes, maybe call it `return_SOMETHING` rather than `render_SOMETHING`.

## 2. Convert Models

Create a private view function that converts your model objects to a JSON-encodable dict.
Have the JSON endpoint respond with that.

## 3. Include AJAX CSRF Setup

Put the [jQuery AJAX Django CSRF setup script](/demos/ajax_csrf_setup.js) in your project's static files folder.
Include it in the HTML just before your JS.

```html
<script src="{% static 'DJANGO_APP_NAME/ajax_csrf_setup.js' %}"></script>
<script src="{% static 'DJANGO_APP_NAME/main.js' %}"></script>
```

## 4. Prepare a Form

Set its action to the JSON view.
We will override the default action.

```html
<form action="{% url 'JSON_VIEW_NAME' %}">
    <textarea name="some-text"></textarea>
    <input type="submit">
</form>
```

1. Overwrite submit event handler
1. Prepare your data
1. Manually submit
1. Have a callback that updates the page.

```js
function submitSource(sourceForm) {
  var actionURL = sourceForm.attr('action');
  var formData = sourceForm.serialize();
  $.post(actionURL, formData).
    always(emptyResponseElements).
    done(fillFromColoredSource).
    fail(fillError);
}
```

The same Python code would process it.
