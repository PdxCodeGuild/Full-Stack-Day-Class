# HTTP Basics

Web browsers communicate via **HTTP** is **Hyper-Text Transport Protocol**.
HTTP is a call and response protocol.

The protocol has no memory on it's own.
But servers and client do.

## HTTP Requests

A request has three basic parts: a **verb**, a **path**, and a **body**.
The path is the same as above.
The body is any input the user has for the server.
The verb is how the server should interpret the body.

Request types are named by their verb.

### GET Request

The most basic request is a GET request.
The verb is `GET`, it has an _empty_ body, and tells the server to simply return the data for the resource it has at the given path.

When you type `www.google.com` in your web browser, it performs a simple GET request to download the main page to show.

```
http://www.google.com/search?q=dinosaurs

GET /search?q=dinosaurs
```

### POST Request

The second most basic request is a POST request.
The verb is `POST`, and it has some data in the body.
It tells the server to incorporate that data _into_ the resource at the given path.
How "into" should be interpreted depends on the server.

When you login to a web site, your web browser performs a POST request to submit your user name and password.

```
http://register-to-vote.com/submit_signup

POST /submit_signup


Name: "David"
Age: "18"
...
```

## HTTP Responses

A response has two basic parts: a **status code** and a **body**.

The status code is a number that represents how the server responded to the request:

* `200 OK`
* `301 MOVED PERMANENTLY`
* `400 BAD REQUEST` your bad
* `403 FORBIDDEN`
* `404 NOT FOUND` nothing at that path
* `500 INTERNAL SERVER ERROR` my bad

For a GET request, the body on a 200 contains the data at the resource;
the page source, image data, etc.

Even non-`200 OK` responses have bodies.
Sometimes they contain error messages.
