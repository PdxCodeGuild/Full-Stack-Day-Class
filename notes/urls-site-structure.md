# Website URL Structure

A **website** is a series of resources that work together to get something done.
**Resources** are pages, images, style information, data, any _noun_.

Resources are identified by their URL or location.
Your web browser knows how to parse the URL and then **request** the data for the resource from the appropriate web server.

The structure of a website is up to you.
There are lots of different ways to use HTML, HTTP, and browsers to make a website that does the right thing.
REST.

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

Routes are nouns.
Have different HTTP verbs update those nouns.

Some special routes might just be verbs.

## Hierarchical Paths

Fun rule: if I chop off any number of path components at the end, I reach a valid path.
