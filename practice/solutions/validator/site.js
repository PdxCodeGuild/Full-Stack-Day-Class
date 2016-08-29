'use strict';

/**
 * Tests wheither a string is a valid full name.
 *
 * A valid full name is FIRST LAST.
 */
function isNameValid(fullName) {
  return /[a-z]+\s[a-z]+/i.test(fullName);
}

/**
 * Tests wheither a string is a valid date of birth.
 *
 * A valid date of birth is YYYY-MM-DD all digits.
 */
function isDateOfBirthValid(dob) {
  return /\d{4}-\d{2}-\d{2}/.test(dob);
}

/**
 * Tests wheither a string is a valid phone number.
 *
 * A valid phone number is DDD-DDD-DDDD all digits.
 */
function isPhoneValid(phoneNumber) {
  return /\d{3}-\d{3}-\d{4}/.test(phoneNumber);
}

/**
 * Update function which displays an input element with an invalid warning.
 */
function updateInputWarning(inputElement, showWarning) {
  if (showWarning) {
    inputElement.addClass('warning');
  } else {
    inputElement.removeClass('warning');
  }
}

/**
 * Main function which runs a full validation on an input element.
 */
function runCheckInputValueValid(inputElement, validationFunction) {
  var inputValue = inputElement.val();
  var isValidValue = inputValue === '' || validationFunction(inputValue);
  updateInputWarning(inputElement, !isValidValue);
}

var fullNameInput = $('#full-name');
var dobInput = $('#dob');
var phoneNumberInput = $('#phone-number');

/**
 * Register handlers so input updates are validated.
 */
function registerEventHandlers() {
  fullNameInput.on('input', function() {
    runCheckInputValueValid(fullNameInput, isNameValid);
  });
  dobInput.on('input', function() {
    runCheckInputValueValid(dobInput, isDateOfBirthValid);
  });
  phoneNumberInput.on('input', function() {
    runCheckInputValueValid(phoneNumberInput, isPhoneValid);
  });
}

$(document).ready(registerEventHandlers);
