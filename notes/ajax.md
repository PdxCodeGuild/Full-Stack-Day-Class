# AJAX Calls

**AJAX** stands for Asynchronous Javascript And XML.
Few use XML anymore, but it has become the name for the general class of technique of updating your _current page_ with _new data from the server_ via JavaScript.

Most responses are JSON these days.
There is a standard called [JSONP](http://stackoverflow.com/questions/2067472/what-is-jsonp-all-about) which allows for secure requests for JSON.

The core jQuery function to do this is `$.ajax()`.
You tell it you want to receive some JSON, the URL to look at, and what arguments to pass as URL query parameters.
It returns (almost a) promise that can be setup to do things when the data comes back.

```js
/**
 * Get the forecast for a given location.
 *
 * Returns a promise.
 */
function getForecast(lat, lng) {
  var PARAMS = {'units': 'us'};
  var url = 'https://api.forecast.io/forecast/' + FORECAST_API_KEY + '/' + lat + ',' + lng;
  return Promise.resolve($.ajax({
    dataType: 'jsonp',
    url: url,
    data: PARAMS
  }));
}

getForecast(0, 0).
  then(function(forecastResponseObjectFromJSON) {
    console.log(forecastResponseObjectFromJSON);
  }).
  catch(function(error) {
    console.log(error);
  });
```

The [docs for ajax()](http://api.jquery.com/jQuery.ajax/) are long and verbose, but has all the details.

You might encounter other HTTP API interfaces than JSONP, and in that case you'll need to look up how to do more low-level GET and POST requests using `ajax()`.
