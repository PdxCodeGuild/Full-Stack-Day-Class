# Practice: Validator
Create a sign-up form for a user to fill out and submit via a button.

It should ask for the following fields:
* Full Name in `First Last` format
* Date of birth in `YYYY-MM-DD` format
* Phone Number in `555-555-5555` format

A field is only valid if it is empty or matches the described format:
* The full name should be two words separated by a space.
Capitalization doesn't matter.
* The date of birth should be three numbers separated by `-`.
The first number should be 4 digits, the second and third 2 digits.
Don't worry about checking the day or month range.
* The phone number should be three numbers separated by `-`.
The first and second should be 3 digits, the third 4 digits.

_As the user is typing_, validate each field.
If the content is currently invalid, the input box should be yellow.

Search for an event that will happen whenever a user modifies an input box.

## Advanced
* Make a yellow warning notice appear beside any field that is invalid.
If it becomes valid, it should disappear.
* Add a submit button.
* If the user submits with valid info, display a green success notice atop the form, otherwise a red error notice.
