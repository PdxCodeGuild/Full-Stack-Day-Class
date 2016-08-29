# Practice: Multi-Madlib

Save your solution in a Django app, directory in `practice/`, and in a branch all named `multimadlib`.
This means there will be a directory `~/codeguild/practice/multimadlib/multimadlib`.

Make a website that allows users to post a madlib template and then fill it out.

There will be four pages:

1.  The **New Madlib** page at `GET /new` will accept a madlib name and Django template string of the madlib text.

    ```
    Down in {{ country }} a {{ adjective_1 }} {{ noun_1 }} was put in the pocket of a kangaroo.
    {{ noun_1|title }} became the kangaroo's best friend!
    ```

    Store some form of this data in your models.

1.  The **Form Page** at `GET /madlib/MADLIB_NAME/form` will have a form that asks for all of the unique template variables and will send them to the rendering page.

    ```html
    <form action="..." method="get">
      <label>country: <input type="text" name="country"></label>
      <label>adjective_1: <input type="text" name="adjective_1"></label>
      <label>noun_1: <input type="text" name="noun_1"></label>
      <input type="submit">
    </form>
    ```

    The ability to [generate Django Template objects from a string](https://docs.djangoproject.com/en/1.10/topics/templates/#django.template.loader.engines) will be helpful here.
    You can then use the following code to find all variable names in that template.

    ```py
    from django.template.base import VariableNode

    def _var_names_in_template(template):
        """Returns a list of all variables names used in a template."""
        return [
            node.filter_expression.var.var
            for node
            in template.compile_nodelist().get_nodes_by_type(VariableNode)
        ]
    ```

1.  A **Madlib Rendering** page at `GET /madlib/MADLIB_NAME` will take in all of the madlib template arguments as query arguments.

    ```
    /kangaroo_lib?Country=China&Adjective_1=spotted&noun_1=lamp
    ```

    Your response body should have the text of the filled out madlib and a `200 OK` response code.
    If any query arguments are missing, respond with a `400 BAD REQUEST` code and a body with a list of the needed argument names.

    The [manual Django template render command](https://docs.djangoproject.com/en/1.10/ref/templates/api/#django.template.Template.render) to be useful here.

1.  A **Listing Page** at `GET /` which has links to all known Form Pages.
