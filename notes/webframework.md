# Web Framework
A **web framework** is a library that does all of the piping for writing a web server for you. The most basic operation is to match URLs with code that should run and produce a response.

You can write a function for each URL in your site, called a [view](django-views.md).
Then link them to the actual URL pattern, called a [route](django-routes.md).
Then fill in the function with whatever code is necessary to produce the HTML content.
It could talk to a DB, another web server, crunch lots of numbers, just read a file, etc.
