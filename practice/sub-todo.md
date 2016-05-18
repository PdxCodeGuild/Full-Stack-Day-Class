# Practice: Sub-Todo

Save your solution in a `sub-todo` directory.

Produce a todo list app that handles sub-items.
Implement your app using Django models to fully persist the list data.

* Buy Groceries +
  - Milk X
  - Spinach X
* Clean House +
  - Dishes X
  - Laundry X

Have each main item have a link to add more sub-items.
Have each sub-item have a link to delete it once it's done.

Make two Django models named:

* `MainItem`
* `SubItem`

Provide a form at the top of the todo list for adding main items.

Use the following URL structure and standard form POSTing:

* `/` shows the todo list.
* `/add` shows a form to add to the list.
* `/submit` is POSTed a new main item, and shows the ack page.
* `/MAIN_ITEM_ID/add` shows the form for adding a new sub-item to that main item.
* `/MAIN_ITEM_ID/submit` is POSTed a new sub-item, and shows the ack page.
* `/MAIN_ITEM_ID/SUB_ITEM_ID/delete` when GET, will delete that sub-item and possibly the main item if empty.

Make sure the admin page is wired up and modifications there are reflected in the main page.

## Advanced

* Instead of using a HTTP GET request on `/MAIN_ITEM_ID/SUB_ITEM_ID/delete` use a HTTP DELETE request on `/MAIN_ITEM_ID/SUB_ITEM_ID`
