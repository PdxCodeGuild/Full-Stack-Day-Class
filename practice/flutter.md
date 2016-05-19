# Practice: Flutter

Save your solution in `practice/flutter`.

Let's make a mini Twitter clone called Flutter where people post Flutts.

* `/` shows the last 10 Flutts.
* `/search?query=QUERY_TEXT` shows the last 10 Flutts containing `QUERY_TEXT` text.
* `/post` is a form to submit a Flutts. There is "user name" and "text".
* `/post/submit` is the ack page. A new Flutt is given the timestamp of the acknowledgement.
* `/USER_NAME` shows the last 10 Flutts by a user.

## Advanced

Use the [Django user auth system](https://docs.djangoproject.com/en/1.9/topics/auth/) to provide:

* A login page at `/login`.
* Only let logged-in users post Flutts.
* Instead of storing "user name" store "user ID" with each Flutt.
* Automatically fill in the user ID of the person logged in when posting a Flutt.
* Change the `/USER_NAME` route to a `/USER_ID` route with the same functionality.
