# Deployment Parts

Running your web app locally is a dance between three separate parts all running on your personal computer:

1. Browser
1. Stateless Python server
1. Stateful SQLite DB

When you **deploy** your app, you are running the Python server on some publicly-accessible, permanent computer, and the database on another permanent computer.

There are lots of cloud hosting options that will manage and make easier the running of your server and DB.
I'll be walking through how to use Heroku here, but there are lots of others.
They span a spectrum of configurability-but-manual-work to automatic-but-not-as-configurable.

So now, you'll have:

1. Random users' browsers
1. Stateless Python server running
1. Stateful PostgreSQL DB running

The only thing that is shared between these two stacks of three parts is _your code_.
The server and database, all the parts controlled by you, is an isolated **environment**.

**The database data is not shared. No data is automatically shared.**
This might be annoying if your app is data-driven, but is part of the model.
This gets at why you don't Git commit your `db.sqlite3` file; the database is an abstraction.

Typically the name given to the environment that serves public web traffic is **production**.
Organizations sometimes might run multiple environments, for testing or staging.

More complicated apps will have way more than two server moving parts.
This kind of design is called a **service oriented architecture**.

* Search service
* Queueing service
* Multiple DBs

All of these have to be replicated or faked in every environment.
