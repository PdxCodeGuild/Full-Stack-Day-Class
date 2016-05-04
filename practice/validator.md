# Practice: Validator
Create a sign-up form for a user to fill out and submit via a button.

It should ask for:
* Full Name in "First Last" format
* Age in YYYY-MM-DD format
* Phone Number in 555-555-5555 format

A "valid" field only matches the syntax of a full name or date.
I don't care that the names are capitalized, that the months are between 1 and 12, etc.

_As the user is typing_, you should validate that the fields are filled in the correct format.
You'll want to look at the various events that get fired when a user is typing, specifically "keyup" or "onblur".
If the content is not currently valid, the field box should be yellow and a yellow warning notice describing which field is malformed displayed atop the form.
If multiple forms are invalid, just show one. I don't care which.
Otherwise, if valid or empty, the fields should be default and no warning notice displayed.

If the user submits with valid info, display a green success notice atop the form, otherwise a red error notice.
