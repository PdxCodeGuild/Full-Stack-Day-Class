# Practice: Timezone

Save your solution in a Django app, directory in `practice/`, in a branch, and make a GitHub Pull Request all named `timezone`.
This means there will be a directory `~/codeguild/practice/timezone/timezone`.

Write a simple HTTP API for getting the local time at various locations around the world.

* `GET /time` returns the current server time
* `GET /LAT,LNG/tz` returns the timezone at a given latitude and longitude as a short description string (e.g. `US/Pacific`)
* `GET /LAT,LNG/time` returns the local time at a given latitude and longitude
* `GET /IN_LAT,IN_LNG/IN_TIME/as/OUT_LAT,OUT_LNG` returns the time at `IN_LAT,IN_LNG` when it is `IN_TIME` at `OUT_LAT,OUT_LNG`.

Serialize all times as [ISO 8601 string format](http://arrow.readthedocs.io/en/latest/#arrow.arrow.Arrow.isoformat).

Use the following Python packages:

* [arrow](http://arrow.readthedocs.io/en/latest/)
* [pytzwhere](https://github.com/pegler/pytzwhere)
