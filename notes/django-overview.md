# Django Overview

First, remind yourself the full [structure of a web app](/notes/web-app-structure.md).

**Django** is a Python library that includes a ton of generic, basic tools for making a dynamic web server.

It gives you web framework to handle the piping involved in a web server and a [ORM](/notes/orm.md) to talk to a database easily.

A **web framework** is a library that does all of the piping for writing a web server for you.
The most basic operation is to match URLs with code that should run and produce a response.
You can write a function for each URL in your site, called a [view](/notes/django-views.md).
Then link them to the actual URL pattern, called a [route](/notes/django-routes.md).
Then fill in the function with whatever code is necessary to produce the HTML content.
It could talk to a DB, another web server, crunch lots of numbers, just read a file, etc.

It also gives you an "admin interface" to your database that auto generates pages that let you debug and inspect the values in there.

## Django isn't a CMS

Django does not directly fill the same role as WordPress or Drupal.
Both of those are **content management systems** or **CMS**.

They give you a pre-made interface to upload content and have it be displayed on a web page.
They are opinionated about the structure of content you can use, although they are extendable through plugins that you can write.
You can those CMSs do all the things you do here, but you'll often be working _against_ it's options rather than working with the basic tools of Django.
