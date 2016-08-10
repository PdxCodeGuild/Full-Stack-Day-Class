'use strict';
// 1. Input Functions

/**
 * Get the reminder string the user typed in.
 */
function getReminderInput() {
  return $('#reminder-input').val();
}

// 2. Transform Functions

// We don't have any since the input reminder string is exactly what we want to
// display.

// 3. Create Functions

/**
 * Create a new "done" link that will cross off the given reminder list item.
 */
function createDoneLink(reminderItem) {
  var doneLink = $('<a></a>');
  doneLink.text('X');
  doneLink.attr('href', '');
  // Part of setting up the "done" link is ensureing it can cross the item off.
  // It's okay to register a callback here.
  doneLink.on('click', function(event) {
    // Prevent clicking on the link from causing the browswer to change the
    // page.
    event.preventDefault();
    runCrossOffReminder(reminderItem);
  });
  return doneLink;
}

/**
 * Create a new reminder list item for a string.
 */
function createReminderItem(reminderString) {
  var reminderItem = $('<li></li>');
  reminderItem.text(reminderString);
  var doneLink = createDoneLink(reminderItem);
  reminderItem.append(doneLink);
  return reminderItem;
}

// 4. Modify Functions

/**
 * Add a reminder list item to the page.
 */
function addReminderItemToList(reminderItem) {
  $('#reminder-list').append(reminderItem);
}

/**
 * Clear the reminder input box.
 */
function clearReminderInput() {
  $('#reminder-input').val('');
}

/**
 * Cross out a given reminder list item.
 */
function crossOffReminder(reminderItem) {
  reminderItem.toggleClass('done');
}

// 5. Main Functions

/**
 * Main function which performs the action of adding a new reminder item with
 * what the user put in the text box.
 */
function runAddReminder() {
  var reminderString = getReminderInput();
  var reminderItem = createReminderItem(reminderString);
  addReminderItemToList(reminderItem);
  clearReminderInput();
}

/**
 * Main function which crosses off a specific reminder item.
 *
 * Which reminder item should be "closed" in when registering the event handler.
 */
function runCrossOffReminder(reminderItem) {
  crossOffReminder(reminderItem);
}

// 6. Register Functions

/**
 * Tell the browser when to run our main function.
 *
 * Note that we can't register the "crossing off" action here because the list
 * items haven't been created yet.
 */
function registerInitialEventHandlers() {
  $('#reminder-form').on('submit', function(event) {
    // Submitting a form, by default, reloads the page. Prevent this.
    event.preventDefault();
    runAddReminder();
  });
}

// Actually run the event handler registration code when the HTML is done
// loading.
$(document).ready(registerInitialEventHandlers);
