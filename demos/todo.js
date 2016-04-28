"use strict";

function getReminderString() {
    return $("#reminder-input").val();
}

function createDelLink(reminderElement) {
    var delLink = $("<a></a>").text("X").attr("href", "");
    delLink.on("click", function (event) {
        event.preventDefault();
        reminderElement.toggleClass("done");
    });
    return delLink;
}

function createReminderElement(reminderString) {
    var reminderElement = $("<li></li>").text(reminderString);
    var delLink = createDelLink();
    return reminderElement.append(delLink);
}

function addReminderElementToList(reminderElement) {
    $("#reminder-list").append(reminderElement);
}

function getReminderStringAndAddElementToList() {
    var reminderString = getReminderString();
    var reminderElement = createReminderElement(reminderString);
    addReminderElementToList(reminderElement);
}

function registerGlobalEventHandlers() {
    $("form").on("submit", function (event) {
        event.preventDefault();
        getItemStringAndAddElement();
    });
}

$(document).ready(function () {
    registerGlobalEventHandlers();
});
