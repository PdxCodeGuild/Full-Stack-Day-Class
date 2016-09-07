'use strict';

// Pre-select all of the elements we'll need for speed.
var form = $('form');
var previewImg = $('#preview');

/**
 * Convert a jQuery XHR response object with image data to a data URI.
 */
function imageResponseToDataURI(data, status, jqXHR) {
  var contentType = jqXHR.getResponseHeader('Content-Type');
  var base64Data = ;
  return 'data:' + contentType + ';base64,' + base64Data;
}

/**
 * Set the URI of the preview image.
 */
function setPreviewSrc(uri) {
  previewImg.attr('src', uri);
}

/**
 * Submit the image and filter form and return a promise with the image response.
 */
function submitForm() {
  var jsonEndpointURL = form.attr('action');
  var jsonEndpointMethod = form.attr('method');
  var formData = new FormData(form[0]);
  return $.ajax({
    url: jsonEndpointURL,
    method: jsonEndpointMethod,
    data: formData,
    processData: false,
    contentType: false
  });
}

/**
 * Main function that runs the form submission, creates a data URI, and displays the image.
 */
function runSubmitImageAndPreview() {
  submitForm().
    then(imageResponseToDataURI).
    then(setPreviewSrc);
}

/**
 * Register that the form should be submitted via AJAX.
 */
function registerEventHndlers() {
  form.on('submit', function(event) {
    event.preventDefault();
    runSubmitImageAndPreview();
  });
}

$(document).ready(registerEventHndlers);
