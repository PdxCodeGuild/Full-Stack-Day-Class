'use strict';

// Select all elements involved in the interactivity up front.
var sourceForm = $('#source-form');
var langNameSpan = $('#lang-name');
var codeDiv = $('#code');
var errorP = $('#error');

/**
 * Fill in the current page with the results of coloring some source text.
 */
function fillFromColoredSource(coloredSourceObj) {
  langNameSpan.text(coloredSourceObj.language);
  codeDiv.html(coloredSourceObj.source_html);
}

/**
 * Fill in the current page with any error encountered during coloring the
 * source text.
 */
function fillError(response) {
  errorP.text(response.responseText);
}

/**
 * Clear all of the fillable elements on the current page in preparation for
 * new data.
 */
function emptyResponseElements() {
  langNameSpan.empty();
  codeDiv.empty();
  errorP.empty();
}

/**
 * Submit the code form and return a promise with the JSON colored source object.
 */
function submitForm() {
  var actionURL = sourceForm.attr('action');
  var submitMethod = sourceForm.attr('method');
  var formData = sourceForm.serialize();
  return Promise.resolve($.ajax({
    dataType: 'json',
    url: actionURL,
    method: submitMethod,
    data: formData
  }));
}

/**
 * Main function that gets data from the source form, POSTs it in the
 * background and updates the page on return.
 */
function runSubmitSourceAndUpdate() {
  // Empty the UI right away so that new data can be loaded.
  emptyResponseElements();
  submitForm().
    // Decode the JSON and call the following function with the resulting JS object.
    then(fillFromColoredSource).
    catch(fillError);
}

/**
 * Register form submit event handler.
 */
function registerGlobalEventHandlers() {
  sourceForm.on('submit', function(event) {
    event.preventDefault();
    runSubmitSourceAndUpdate();
  });
}

// Register handlers for permanent elements on the page.
$(document).ready(registerGlobalEventHandlers);
