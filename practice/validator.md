# Practice: Validator
Create a sign-up form for a user to fill out and submit via a button.

It should ask for:
* Full Name in "First Last" format
* Age in YYYY-MM-DD format
* Phone Number in 555-555-5555 format

_As the user is typing_, you should validate that the fields are filled in the correct format.
If the content is not currently valid, the field box should be yellow and a yellow warning notice describing which field is malformed displayed atop the form.
If multiple forms are invalid, just show one. I don't care which.
Otherwise, if valid or empty, the fields should be default and no warning notice displayed.

If the user submits with valid info, display a green success notice atop the form, otherwise a red error notice.
