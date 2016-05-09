# Practice: Multi-Madlib
Put your solution in a directory named `multi_madlib`.
Your solution should be a full-fledged Django and Python application.

Make a website that fills in madlibs, served by Django.
Find or make up three madlibs with at least three word slots each.

Make a page for each madlib;
come up with some short name for each one, e.g. `/kangaroo_lib`.
Have it take in query arguments for each missing word, e.g. `/kangaroo_lib?noun_1=house`.

Respond with the text of the filled out madlib and a `200 OK` response code.
If any query arguments are missing, respond with a `400 BAD REQUEST` and a list of the needed argument names in the body.
