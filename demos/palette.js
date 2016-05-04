'use strict';
// 1. Input Functions

/*
Get the input string of unit component colors.
*/
function getUnitColorString() {
  return $('#color-input').val();
}

// 2. Transform Functions

/*
Take a unit color value between 0 and 1 and return it as a byte color value between 0 and 255 as an "int".
*/
function renormalizeColorNumber(unitValue) {
  return Math.round(unitValue * 255);
}

/*
Renormalize a unit color value stored as a string and return it as a string.

This is to conveniently be able to create a CSS color.
*/
function renormalizeColorString(unitValueString) {
  var unitValue = Number(unitValueString);
  var byteValue = renormalizeColorNumber(unitValue);
  return String(byteValue);
}

/*
Take the raw user input which looks like "0 1 0" and convert it to a CSS color string like "rgb(0, 255, 0)".
*/
function convertUnitColorStringToCSSColor(unitColorString) {
  var unitColorStringArray = _.split(unitColorString, ' ');
  var byteColorStringArray = _.map(
    unitColorStringArray,
    renormalizeColorString);
  var byteColorString = _.join(byteColorStringArray, ', ');
  return 'rgb(' + byteColorString + ')';
}

/*
Return a boolean if a single number is a valid unit color component.

Valid components are between 0 and 1 inclusive.
*/
function isUnitColorValid(unitColor) {
  return unitColor <= 1.0 && unitColor >= 0.0;
}

/*
Return a boolean if a string matches the format "0 1 0".

There must be three valid unit color component numbers.
*/
function isUnitColorStringValid(unitColorString) {
  var unitColorStringArray = _.split(_.trim(unitColorString), ' ');
  if (unitColorStringArray.length !== 3) {
    return false;
  }
  var unitColorArray = _.map(unitColorStringArray, Number);
  if (!_.every(unitColorArray, isUnitColorValid)) {
    return false;
  }

  return true;
}

// 3. Create Functions

// We have no create functions. All the elements we want to modify already exist.

// 4. Modify Functions

/*
Show or hide the error message.
*/
function showError(show) {
  $('#format-error').css('display', show ? 'block' : 'none');
}

/*
Update the swatch's background color with a CSS color string.
*/
function changeSwatchBackground(cssColor) {
  $('#color-swatch').css('background', cssColor);
}

// 5. Main Functions

/*
Main function that will show an error if the color string is invalid.
*/
function runValidateUnitColorString() {
  var unitColorString = getUnitColorString();
  var displayError = !isUnitColorStringValid(unitColorString);
  showError(displayError);
}

/*
Main function which parses the input color and updates the div to that.
*/
function runUpdateColor() {
  var unitColorString = getUnitColorString();
  // Only update the color if it's valid.
  if (isUnitColorStringValid(unitColorString)) {
    var cssColor = convertUnitColorStringToCSSColor(unitColorString);
    changeSwatchBackground(cssColor);
  }
}

// 6. Register Functions

/*
Tell the browser when to run our main functions.

You can register multiple handler functions for the same event. They are all run.
*/
function registerInitialEventHandlers() {
  $('#color-input').on('input', runValidateUnitColorString);
  $('#color-input').on('input', runUpdateColor);
}

// Actually run the event handler registration code when the HTML is done loading.
$(document).ready(function() {
  // Run the mains now so that the display is synchronized to the default value in the input before any events have been fired.
  runValidateUnitColorString();
  runUpdateColor();

  registerInitialEventHandlers();
});
