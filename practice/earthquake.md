# Practice: Earthquake

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `earthquake`.
Your HTML file should be named `index.html`, your CSS file named `site.css`, and your JS file named `site.js` in that directory.

The [USGS has feeds of earthquake locations](http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php).
Using their feed of [all earthquakes over the past seven days](http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson), and the [OpenLayers](http://openlayers.org) JS library, create a map visualization of all of the earthquakes.

* Asynchronously download the most recent earthquake data
* Display earthquake locations on a map as dots
* Have the size of each dot correspond to the strength of the earthquake
* Have the opacity of each dot correspond to how old the earthquake event is

Map **projections** are a pretty complicated topic to fully understand, but for this problem you only need to know two basic facts.
The points from the data source are in the EPSG:4326, or WGS84 or latitude and longitude in degrees.
Almost all web maps use EPSG:3857, or Web Mercator projection, and OpenLayers uses that by default on basic maps.
Thus, if you want to properly render a latitude longitude pair on those maps, run it through [ol.proj.fromLonLat([lon, lat])](http://openlayers.org/en/latest/apidoc/ol.proj.html#.fromLonLat) first and add that to the map source.

## Advanced

* The feed is updated every five minutes, so have your page automatically fetch new data on that interval.

## Super Advanced

Display a special animation for new earthquake points.

There's some animation functions as part of GeoJS.
CSS animations also might come in handy.
