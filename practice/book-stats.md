# Practice: Book Stats
Put your solution in a directory named `book_stats`.
It should be a full-fledged Django and Python application.

Make a "website" version of your [word count practice](wordcount.md).

It should have one page that takes one argument that is the word you want the count for, `/count?w=WORD`.
Respond with a `200 OK` code and a body containing `WORD: COUNT`.
If the word doesn't exist in the book, still respond with a `200 OK` code but return a zero count in the body.

Place your word counting logic in a `logic.py` module in the application root.
(Feel free to copy your solution from before.)
Have that module, _on import_ load the word counts.
Have your view functions `from . import logic` and call the counting functions.
Don't put the counting logic in the views.

## Advanced
Make a second page `/` that presents an HTML form that lets the user enter a word.

Use JS events and [jQuery's AJAX](http://api.jquery.com/jQuery.ajax/) function to request the count for that word and dynamically update the page with the count.
