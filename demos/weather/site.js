'use strict';

var FORECAST_API_KEY = ;

/**
 * Update the location header with a new location.
 */
function updateLocationHeader(lat, lng) {
  $('#location').text(lat + ', ' + lng);
}

/**
 * Update the forecast paragraph with some text.
 */
function updateForecastParagraph(forecastText) {
  $('#forecast').text(forecastText);
}

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

/**
 * Create a string description from a forecast.
 */
function formatForecastResult(forecastResult) {
  return 'Temp: ' + forecastResult.currently.temperature + ' F';
}

/**
 * Main which gets a forecast and updates the UI for a location.
 */
function runForecast(lat, lng) {
  updateLocationHeader(lat, lng);
  updateForecastParagraph('Loading...');

  getForecast(lat, lng).
    then(function(forecastResult) {
      var forecastText = formatForecastResult(forecastResult);
      updateForecastParagraph(forecastText);
    }).
    catch(function(error) {
      updateForecastParagraph('Error occured. ' + error.statusText);
    });
}

/**
 * Return the element to be used as a Google Map.
 */
function getMapElement() {
  return $('#map')[0];
}

/**
 * Create a Google Map on a given element and return the map object.
 */
function createMap(mapElement) {
  return new google.maps.Map(mapElement, {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
  });
}

/**
 * Register event handlers on the map.
 *
 * Clicks will run the forecast main on the location clicked.
 */
function registerMapEventHandlers(map) {
  map.addListener('click', function(event) {
    var lat = event.latLng.lat();
    var lng = event.latLng.lng();
    runForecast(lat, lng);
  });
}

/**
 * Initialize the page on load.
 */
function runInitPage() {
  var mapElement = getMapElement();
  var map = createMap(mapElement);
  registerMapEventHandlers(map);
  // Setup some initial values.
  runForecast(map.center.lat(), map.center.lng());
}

$(document).ready(runInitPage);
