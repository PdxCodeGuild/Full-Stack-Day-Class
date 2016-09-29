# Configuration Levels

Now we have this problem.
Our application code has to be identical between running locally for development and in production.
But we want it to behave differently!

* It needs to talk to a PostgreSQL database hosted on a different computer.
* It needs to not run in debug mode.
* It needs to have a truly secret secret key (not checked into public source).
* It needs to [securely serve static files](https://docs.djangoproject.com/en/1.10/howto/static-files/).
* It needs to [write user uploaded files](https://docs.djangoproject.com/en/1.10/topics/files/) somewhere persistent (the while stateless server computer also must be stateless).

All of those things relate to what's in `settings.py`.
So we need a way of having a single checked-in `settings.py` modify its behavior based on what environment it's running in.

This trick is generally called **configuration levels**.
There are lots of different practical ways to do this:

* Sometimes the config lives in a special file that is loaded.
* Sometimes the config has a hierarchy of overwriting settings.
* Sometimes the config is provided by an HTTP API.

Conveniently, we have **environment variables**!

Our goal:
Have our `settings.py` file look in special environment variables.
If they do exist, connect to that DB or use a different secret key or etc.
If they don't exist, run in development mode and assume the Python server is running on your local computer.

[Put all of your secrets in environment variables.](/notes/secrets.md)
Even if they are needed when running locally.
