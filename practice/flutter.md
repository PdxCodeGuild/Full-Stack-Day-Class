# Practice: Flutter

Save your solution in a Django app, directory in `practice/`, in a branch, and in a Pull Request all named `flutter`.
This means there will be a directory `~/codeguild/practice/flutter/flutter`.

Let's make a mini Twitter clone called Flutter where people post Flutts.
A single Flutt just contains some text and a timestamp.
A new Flutt is given the timestamp of receiving the data.

* `GET /` shows the last 10 Flutts from most to least recent
* `GET /search?query=QUERY_TEXT` shows the last 10 Flutts containing `QUERY_TEXT` text from most to least recent
* `GET /post` shows a form to submit a Flutts
* `POST /post/submit` accepts the new flut data and shows the ack page.

Configure the admin interface to display Flutt model.

## Super Advanced

Use the [Django user auth system](https://docs.djangoproject.com/en/1.9/topics/auth/) to provide:

* A login page at `GET /login`
* Only let logged-in users post Flutts
* Automatically fill in the user ID of the person logged in when posting a Flutt
* Add displaying the user name to all of the other Flutt pages
* Add a `GET /user/USER_ID` route which shows the last 10 Flutts of a given user from most to least recent
