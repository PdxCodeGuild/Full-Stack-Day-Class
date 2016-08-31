# Practice: Sub-Todo

Save your solution in a Django app, directory in `practice/`, and in a branch all named `sub_todo`.
This means there will be a directory `~/codeguild/practice/sub_todo/sub_todo`.

Produce a todo list app that handles sub-items.
Implement your app using Django models to fully persist the list data.

*   Buy Groceries +

    * Milk X
    * Spinach X

*   Clean House +

    * Dishes X
    * Laundry X

Have a link at the top to a page to add a main item.
Have each main item have a link `+` to add more sub-items.
Have each sub-item have a link `X` to delete it once it's done.

Make two Django models named:

* `MainItem`
* `SubItem`

Use the following URL structure:

* `GET /` shows the todo list
* `GET /add` shows a form to add a main item to the list
* `POST /submit` is POSTed a new main item, and shows the ack page
* `GET /MAIN_ITEM_ID/add` shows the form for adding a new sub-item to that main item
* `POST /MAIN_ITEM_ID/submit` is POSTed a new sub-item, and shows the ack page
* `DELETE /MAIN_ITEM_ID/SUB_ITEM_ID` will delete that sub-item and possibly the main item if empty; jQuery AJAX calls can be used to send DELETE HTTP requests

Make sure the admin page is wired up and modifications there are reflected in the main page.
