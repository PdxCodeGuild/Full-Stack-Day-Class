# Practice: Earthquake

The [USGS has feeds of earthquake locations](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).
Using their feed of [all earthquakes over the past seven days](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson), and the [GeoJS](http://geojs.readthedocs.io/en/latest/index.html) library, create a map visualization of all of the earthquakes.

* Asynchronously download the most recent earthquake data
* Display earthquake locations on a map as dots
* Have the size of each dot correspond to the strength of the earthquake
* Have the opacity of each dot correspond to how old the earthquake event is

## Advanced

* The feed is updated every five minutes, so have your page automatically fetch new data on that interval.
* Display a special animation for new earthquake points.
