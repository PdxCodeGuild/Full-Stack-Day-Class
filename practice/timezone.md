# Practice: Timezone

Save your solution in a Django app, directory in `practice/`, in a branch, and make a GitHub Pull Request all named `timezone`.
This means there will be a directory `~/codeguild/practice/timezone/timezone`.

Write a simple HTTP API for getting the local time at various locations around the world.
When I refer to **time** below, I mean a full date, local time, and timezone information.

*   `GET /time` returns the current time in the server's timezone.

    ```
    GET /time

    2016-08-25T17:27:45.556703+00:00
    ```

*   `GET /LAT,LNG/tz` returns the timezone at a given latitude and longitude as a short description string (e.g. `America/Los_Angeles`).
    If there is no timezone at that location, return a 404.

    ```
    GET /35.29,-89.66/tz

    America/Chicago
    ```

*   `GET /LAT,LNG/time` returns the current time in the timezone at a given latitude and longitude.
    If there is no timezone at that location, return a 400.

    ```
    GET /35.29,-89.66/time

    2016-08-25T12:27:15.999611-05:00
    ```

*   `GET /TIME/at/LAT,LNG` returns the time in the timezone at at a given latitude and longitude when it is `TIME` in some other timezone.
    If there is no timezone at that location, return a 400.

    ```
    GET /2016-08-25T10:40:15-07:00/at/35.29,-89.66

    2016-08-25T12:40:15-05:00
    ```

Serialize all times in fully specified [ISO 8601 date, time, and timezone string format](http://arrow.readthedocs.io/en/latest/#arrow.arrow.Arrow.isoformat).

If any of the latitude or longitude or time input data is improperly formatted, return a `400 BAD REQUEST`.
Don't worry about having the route regular expressions match the ISO format; instead check for validity during parsing into an Arrow object.

Use the following Python packages:

* [arrow](http://arrow.readthedocs.io/en/latest/)
* [tzwhere](https://github.com/pegler/pytzwhere)
