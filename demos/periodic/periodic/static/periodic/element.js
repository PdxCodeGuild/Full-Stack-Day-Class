'use strict';

// Pre-query for reactive elements so we don't have to look them up on every mouseover.
var ionicText = $('#ionic-li');
var atomicText = $('#atomic-li');

/**
 * Show just the ionic radius text.
 */
function showIonicRadius() {
  ionicText.show();
  atomicText.hide();
}

/**
 * Show just the atomic radius text.
 */
function showAtomicRaidus() {
  atomicText.show();
  ionicText.hide();
}

/**
 * Register event handlers so ionic radius is shown only on mouseover.
 */
function registerEventHandlers() {
  atomicText.on('mouseenter', showIonicRadius);
  ionicText.on('mouseleave', showAtomicRaidus);
}

/**
 * Visually mark the hoverable text.
 *
 * Do this in JS so that before the JS is loaded / if it's not loaded, the page displays correctly.
 */
function markHover() {
  atomicText.addClass('hover-mark');
  ionicText.addClass('hover-mark');
}

$(document).ready(function() {
  registerEventHandlers();
  markHover();

  // Start off by hiding the ionic radius.
  showAtomicRaidus();
});
