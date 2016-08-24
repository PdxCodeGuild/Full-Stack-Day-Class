# Template Debugging

Templates are basically just printing things out already, so it's easy to debug them by using simple variable interpolation with `{{}}`.
Then you can load the page and see what the values are.

Structured values like dicts or class instances will be repr'd.

```py
def render_index(request):
    template_arguments = {
        'posts': [
            {'author': 'David', 'post_date': '2016-01-01'},
            {'author': 'Helen', 'post_date': '2016-02-02'},
        ],
    }
    return render(request, 'index.html', template_arguments)
```

If your template prints a structured item, you'll get the repr.

```html
{{ posts }}
```

The resulting rendered HTML will be

```html
[{'author': 'David', 'post_date': '2016-01-01'}, {'author': 'Helen', 'post_date': '2016-02-02'}]
```

which is easy to debug.
