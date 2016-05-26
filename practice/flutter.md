# Practice: Flutter

Save your solution in `practice/flutter`.

Let's make a mini Twitter clone called Flutter where people post Flutts.
A single Flutt just contains some text.

* `/` shows the last 10 Flutts.
* `/search/QUERY_TEXT` shows the last 10 Flutts containing `QUERY_TEXT` text.
* `/post` is a form to submit a Flutts.
* `/post/submit` is the ack page. A new Flutt is given the timestamp of the acknowledgement.

## Advanced

Use the [Django user auth system](https://docs.djangoproject.com/en/1.9/topics/auth/) to provide:

* A login page at `/login`.
* Only let logged-in users post Flutts.
* Instead of storing "user name" store "user ID" with each Flutt.
* Automatically fill in the user ID of the person logged in when posting a Flutt.
* Add a `/user/USER_ID` route which shows the last 10 Flutts of a given user.
