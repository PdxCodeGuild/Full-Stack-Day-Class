# AJAX
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
