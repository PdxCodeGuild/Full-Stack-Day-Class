'use strict';

var map;
var mapElement = $('#map');

function initMap() {
  var lat = mapElement.data('lat');
  var lng = mapElement.data('lng');
  map = new google.maps.Map(mapElement[0], {
    center: {lat: lat, lng: lng},
    zoom: 8
  });
}

$(document).ready(initMap);
