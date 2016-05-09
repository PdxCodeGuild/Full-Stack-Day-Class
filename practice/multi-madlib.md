# Practice: Multi-Madlib
Put your solution in a directory named `multi_madlib`.
It should be a full-fledged Django and Python application.

Make a "website" that fills in madlibs, served by Django.
Find or make up three madlibs with at least three word slots each.

Make a page for each madlib;
come up with some short name for each one, e.g. `/kangaroo_lib`.
Have it take in query arguments for each missing word, e.g. `/kangaroo_lib?noun_1=house`.

Your response body should have the text of the filled out madlib and a `200 OK` response code.
If any query arguments are missing, respond with a `400 BAD REQUEST` code and a body with a list of the needed argument names.

Don't worry about responding with fully-formed HTML or having a form for input.
Someone using your website will have to manually construct the query arguments.
