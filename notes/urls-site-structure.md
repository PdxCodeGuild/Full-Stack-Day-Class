# Website URL Structure

A **website** is a series of resources that work together to get something done.
**Resources** are pages, images, style information, data, any _noun_.

Resources are identified by their URL or location.
Your web browser knows how to parse the URL and then **request** the data for the resource from the appropriate web server.

The structure of a website is up to you.
There are lots of different ways to use HTML, HTTP, and browsers to make a website that does the right thing.

## Impedance Mismatch

The [impedance mismatch](/notes/apis-http.md#httpimpedancemismatch) you felt when working with HTTP APIs now comes front and center.

Effectively, we're writing an HTTP API and an application that is going to be consumed by the browser and the JS.
Browsers only make HTTP requests.
Each request solicits one response.
How do we communicate and keep track of data between pages?
Between sessions?

You'll have to come up with some consistent way to use the models HTTP and the browser gives you to make something functional and that reasonably interfaces with JS and Python.

That's a challenge at first!

## General Site Patterns

Routes are nouns + verbs.
`GET` requests just retrieve data and never change it.
`POST` requests can change data.

```
GET /products/PRODUCT_NAME/images
POST /images
POST /user/USER_ID/image
```

### REST

Some folks have tried to formalize how HTTP interfaces and websites should be laid out.
One of those methods is called **REST**.
[Read up on it](http://www.restapitutorial.com/lessons/whatisrest.html) if you're interested, but I'm not going to require you to use it.

## Hierarchical Paths

Fun rule: if I chop off any number of path components at the end, I reach a valid path.
