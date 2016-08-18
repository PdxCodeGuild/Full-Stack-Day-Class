'use strict';

/**
 * Return a promise that will contain the current device position.
 */
function getCurrentPosition(options) {
  return new Promise(function(resolve, reject) {
    navigator.geolocation.getCurrentPosition(resolve, reject, options);
  });
}

/**
 * Extract a latitude, longitude pair array from a geolocation position result.
 */
function extractLatLng(position) {
  return [position.coords.latitude, position.coords.longitude];
}

/**
 * Return a promise with stop location result object from TriMet.
 */
function getNearbyStops(latLng) {
  return Promise.resolve($.ajax({
    dataType: 'jsonp',
    url: 'https://developer.trimet.org/ws/V1/stops',
    data: {
      appID: TRIMET_APP_ID,
      json: true,
      ll: latLng.join(','),
      meters: 100,
      showRoutes: true
    }
  }));
}

/**
 * From a stop location result object return a list of all unique routes in all stops found.
 */
function extractUniqueRoutes(stopResponse) {
  var allRoutes = _.flatMap(
    stopResponse.resultSet.location,
    function(location) {
      return location.route;
    });
  return _.filter(_.uniq(allRoutes), function(route) {
    return route !== undefined;
  });
}

/**
 * From a route object, return a link to the TriMet schedule page.
 */
function createRouteLink(route) {
  var paddedNum = _.padStart(route.route, 3, '0');
  return 'http://trimet.org/schedules/r' + paddedNum + '.htm';
}

/**
 * Create a new list item for a route object.
 */
function createListItemForRoute(route) {
  var link = $('<a></a>').
    attr('href', createRouteLink(route)).
    text(route.desc);
  return $('<li></li>').append(link);
}

/**
 * Return an array of list items for all routes.
 */
function createListItemsForRoutes(routes) {
  return _.map(routes, createListItemForRoute);
}

// Store a link to the route unordered list element right off the bat.
var routeList = $('#route-list');

/**
 * Update the route list to a pre-made list of route items.
 */
function updateRouteListWithItems(routeItems) {
  routeList.empty();
  routeList.append(routeItems);
}

/**
 * Update the route list to display just "Loading...".
 */
function updateRouteListWithLoading() {
  routeList.empty();
  routeList.text('Loading...');
}

// Keep track of all markers currently on the map.
// There is no other way to get this information so we have to bookkeep it ourselves.
// Only modify this with updateMapWithMarkers().
var mapMarkers = [];
// Make a map and save it for later modification with the below functions.
var map = new google.maps.Map(
  $('#map')[0],
  {
    center: {lat: -34.397, lng: 150.644},
    scrollwheel: false,
    zoom: 8,
    maxZoom: 17
  });

/**
 * Move the map to center on a location.
 */
function moveMapTo(latLng) {
  map.panTo({lat: latLng[0], lng: latLng[1]});
}

/**
 * Convert a single stop object from the TriMet response into a map marker.
 */
function createMarkerForStop(stopLocation) {
  return new google.maps.Marker({
    position: {lat: stopLocation.lat, lng: stopLocation.lng},
    title: stopLocation.desc
  });
}

/**
 * Convert an array of stop objects from the TriMet response into an array of map markers.
 */
function createMarkersForStops(stopResponse) {
  return _.map(stopResponse.resultSet.location, createMarkerForStop);
}

/**
 * From an array of map markers, calculate the bounds that will display them all.
 */
function calcBoundsOfMarkers(stopMarkers) {
  var bounds = new google.maps.LatLngBounds();
  _.forEach(stopMarkers, function(marker) {
    bounds.extend(marker.getPosition());
  });
  return bounds;
}

/**
 * Change all markers on the map to be the given array of markers.
 */
function updateMapWithMarkers(stopMarkers) {
  // Remove all of the old markers.
  _.forEach(mapMarkers, function(oldMarker) {
    oldMarker.setMap(null);
  });

  // Save the new markers.
  mapMarkers = stopMarkers;

  // Calculate bounds to display those markers.
  var markerBounds = calcBoundsOfMarkers(mapMarkers);
  map.fitBounds(markerBounds);

  // Add all of the new markers.
  _.forEach(mapMarkers, function(marker) {
    marker.setMap(map);
  });
}

/**
 * Main function that runs location finding and updating map and route list.
 */
function runLocateAndUpdate() {
  updateRouteListWithLoading();
  getCurrentPosition().
    then(extractLatLng).
    then(function(latLng) {
      // Before we get a response from TriMet and can get a good center bounds, estimate it by moving the map to the current location.
      moveMapTo(latLng);
      // Thread through the TriMet stop response promise to the rest of this chain.
      return getNearbyStops(latLng);
    }).
    // Perform all of the final updates synchronously.
    then(function(stopResponse) {
      // Filter input data.
      var stopMarkers = createMarkersForStops(stopResponse);
      var uniqRoutes = extractUniqueRoutes(stopResponse);

      // Create updated elements.
      var routeItems = createListItemsForRoutes(uniqRoutes);

      // Update current DOM.
      updateMapWithMarkers(stopMarkers);
      updateRouteListWithItems(routeItems);
    });
}

$(document).ready(runLocateAndUpdate);
