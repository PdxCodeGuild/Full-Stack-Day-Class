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

## 5. Prepare a Main

Write a "main" function in your site's JS that will query the form, and kick off a async POST request.
The two exciting parts.

1. Use `.serialize()` to get the data entered in a form
1. Use `$.post(ACTION_URL, FORM_DATA)` to actually kick off the request.

On the call to `post()` you can add various callback functions to run on success or failure.
They will be called in order.

* `done(successCallback)` is given a function that can process completed and decoded JSON object
* `fail(failureCallback)` is given a function that can process an error response
* `always(doneCallback)` is given a function that will run in either case

```js
function emptyPage() {
    ...
}

function fillPageWithResults(jsonObj) {
    ...
}

function fillPageWithError(jqXHR) {
    jqXHR.responseText;
    ...
}

function runSubmitAndUpdate() {
  var sourceForm = $('#my-form');
  var actionURL = sourceForm.attr('action');
  var formData = sourceForm.serialize();
  $.post(actionURL, formData).
    always(emptyPage).
    done(fillPageWithResults).
    fail(fillPageWithError);
}
```

Check out the [jQuery jqXHR object documentation](http://api.jquery.com/jQuery.ajax/#jqXHR) for further details on how to use those functions.
