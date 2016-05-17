# Logic in Web Apps
Try to separate out the core logic of your web app from the HTTP parts.

View functions shouldn't deal directly with the DB or persistent state.
Logic functions shouldn't have references to requests or templates.
Instead have them call logic functions in a separate module.

This is a continuation of the program structuring techniques you already know.
