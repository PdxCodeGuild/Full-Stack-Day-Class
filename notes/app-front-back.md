# Front-End vs Back-End

Now with the ability to template and make arbitrary AJAX calls, there are two places you can put almost any of your code:

1. JS / Front-End
1. Python / Back-End

Keep the JS / front end limited to just _interface interactivity_ code.
Do all of your _business logic_ or data processing in the back end in Python.

Your goal is to move the least amount and complexity of data between server and your JS.
Or between original dataset and DB.

Err on the side of pre-processing as much of your data as possible.
Have a script you manually run once, and it makes nice clean versions of your data, and save that in the DB or in a separate file.
Then you web sever just reads the clean data.
