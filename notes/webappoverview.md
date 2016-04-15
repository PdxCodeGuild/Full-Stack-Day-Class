# High-Level Structure of a Web App
A web application has three big moving parts:
1. Database
1. Back-End
1. Front-End

## Database
This is where your data is persistently stored.
It is another program that has a very generic interface that lets you save and fetch data.

You don't write this part.
E.g. [PostgreSQL](http://www.postgresql.org).

## Back-End
This is your **web server**.
It serves dynamically generated web pages.
When someone goes to `www.yourwebsite.com/show/ponies`, it will figure out what's on that page, maybe by talking to the database or other web sites, and return the content associated with it for display.

This is the code you write in **Python**.
It contains your **business logic**.
You will use a **web framework** that handles all of the input and output;
all you have to do is figure out how to generate output **content** for an input **path**.

## Front-End
This is the **HTML**, **CSS**, and **Javascript** that your web server returns.
The HTML is the actual structured content that your server wants to show the user.
The CSS describes the presentation of the content.
The Javascript is code for the user's web browser to run to enable complex interactions with the user.
