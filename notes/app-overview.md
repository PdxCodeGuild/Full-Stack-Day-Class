# High-Level Structure of a Web App

A web application has three big moving parts:

1. Database
1. Back-End
1. Front-End

## Database

This is the **persistent datastore**.
Every other part of the app is _stateless_ and can't "remember" things.
It is another program that somebody else wrote that lets you save and fetch data.

We're gonna be using SQL or Structured Query Language databases, but we will use an [ORM](/notes/orm.md) to interface with them and will not be discussing SQL.

## Back-End

This is your **web server**.
It serves dynamically generated web pages.
When someone goes to `www.yourwebsite.com/show/ponies`, it will figure out what's on `/show/ponies`, maybe by talking to the database or other web sites, and return the content associated with it for display.

This is the code you write in **Python**.
It contains your _business logic_.
You will use a **web framework** that handles all of the input and output;
all you have to do is figure out how to generate output **content** for an input **path**.

## Front-End

This is the **HTML**, **CSS**, and **JavaScript** that your web server returns.
The HTML is the actual structured content that your server wants to show the user.
The CSS describes the presentation of the content.
The JavaScript is code for the user's web browser to run to enable complex _interactions_ with the user.
