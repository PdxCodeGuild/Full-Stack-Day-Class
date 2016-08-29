# Advanced Website URL Structure

We've learned a few different ways to use the URLs of our site:

* Static Paths - `/login`
* Path Parameters - `/profile/USER_ID`
* Posting - `/post/form` and `/post/submit`
* Query Parameters - `/search?query=snuggies`

Here's a quick overview of the conventions surrounding when you use each.
Remember, there are tons of different conventions (e.g. REST, required arguments as path params, etc.) but here are my guidelines.

*   Have your views represent nouns, or views of nouns.

*   Use path parameters if the thing your viewing has a "name" and the server already knows about it.

*   Use query parameters if there are optional "arguments" to the view, especially if the argument is user supplied.
    Never use a query parameter view to update data on the server.

*   If you need to update data on the server, use a form and post.
