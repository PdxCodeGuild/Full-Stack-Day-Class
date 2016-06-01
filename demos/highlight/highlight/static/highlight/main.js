'use strict';

/**
 * Fill in the current page with the results of coloring some source text.
 */
function fillFromColoredSource(coloredSourceObj) {
  var langNameSpan = $('#lang-name');
  langNameSpan.text(coloredSourceObj.language);
  var codeDiv = $('#code');
  codeDiv.html(coloredSourceObj.source_html);
}

/**
 * Fill in the current page with any error encountered during coloring the
 * source text.
 */
function fillError(response) {
  var errorP = $('#error');
  errorP.text(response.responseText);
}

/**
 * Clear all of the fillable elements on the current page in preparation for
 * new data.
 */
function emptyResponseElements() {
  var langNameSpan = $('#lang-name');
  langNameSpan.empty();
  var codeDiv = $('#code');
  codeDiv.empty();
  var errorP = $('#error');
  errorP.empty();
}

/**
 * Main function that gets data from the source form, POSTs it in the
 * background and updates the page on return.
 */
function runSubmitSourceAndUpdate() {
  var sourceForm = $('#source-form');
  var actionURL = sourceForm.attr('action');
  var formData = sourceForm.serialize();
  $.post(actionURL, formData).
    always(emptyResponseElements).
    done(fillFromColoredSource).
    fail(fillError);
}

/**
 * Register form submit event handler.
 */
function registerGlobalEventHandlers() {
  var sourceForm = $('#source-form');
  sourceForm.on('submit', function(event) {
    event.preventDefault();

    runSubmitSourceAndUpdate();
  });
}

// Register handlers for permanent elements on the page.
$(document).ready(registerGlobalEventHandlers);
