# Practice: Flutter

Save your solution in a Django app, directory in `practice/`, in a branch, and in a Pull Request all named `flutter`.
This means there will be a directory `~/codeguild/practice/flutter/flutter`.

Let's make a mini Twitter clone called Flutter where people post Flutts.
A single Flutt just contains some text.

* `GET /` shows the last 10 Flutts
* `GET /search?query=QUERY_TEXT` shows the last 10 Flutts containing `QUERY_TEXT` text
* `GET /post` is a form to submit a Flutts
* `POST /post/submit` is the ack page. A new Flutt is given the timestamp of the acknowledgement

## Advanced

Use the [Django user auth system](https://docs.djangoproject.com/en/1.9/topics/auth/) to provide:

* A login page at `GET /login`
* Only let logged-in users post Flutts
* Instead of storing "user name" store "user ID" with each Flutt
* Automatically fill in the user ID of the person logged in when posting a Flutt
* Add a `GET /user/USER_ID` route which shows the last 10 Flutts of a given user
