# Practice: Validator
Create a sign-up form for a user to fill out and submit via a button.

It should ask for the following fields:
* Full Name in `First Last` format (capitalization doesn't matter)
* Age in `YYYY-MM-DD` format (validating the range of MM or DD doesn't matter)
* Phone Number in `555-555-5555` format

A field is only valid if it is empty or matches the described format.

_As the user is typing_, validate each field.
If the content is currently invalid, the input box should be yellow.

Search for an event that will happen whenever a user modifies an input box.
You'll use a new one we haven't encounterd yet.

## Advanced
* Make a yellow warning notice appear beside any field that is invalid.
If it becomes valid, it should disappear.
* Add a submit button.
* If the user submits with valid info, display a green success notice atop the form, otherwise a red error notice.
