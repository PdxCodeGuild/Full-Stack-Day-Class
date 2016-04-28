# Front-End vs Back-End
There are two places you can put your code

Keep the front end limited to just interface interactivity code.
Do all of your data processing in the backed in python.

Your goal is to move the least amount and complexity of data between server and your JS.
Or between original dataset and DB.

Err on the side of pre-processing as much of your data as possible.

You can do "offline processing".
Have a script you manually run once, and it makes nice clean versions of your data, and save that in the DB or in a separate file.
Then you web sever just reads the clean data.

No need to do all the work every time.
