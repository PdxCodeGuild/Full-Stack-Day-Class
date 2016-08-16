# HTTP APIs

Many companies expose some functionality over an HTTP API.

## Requests

Usually requests involve constructing a GET request:

1. A URL with a path that roughly corresponds to what "function" you want to call
1. Setting URL query parameters with "arguments"

```
https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE?units=UNIT
```

If the "function" you're calling modifies data, sometimes it has to be a POST request and data is placed in the POST body.

## Responses

Most HTTP APIs these days respond with JSON in the body.

## REST

A very specific style of formatting requests and responses is called **REpresentational State Transfer** or **REST**.
These APIs usually have their URL paths correspond to a strict hierarchy of nouns, then use all of the HTTP verbs in order to manipulate those nouns.

```
GET /users/USER_ID/friends
PUT /users/USER_ID
DELETE /users/USER_ID/friends/FRIEND_ID
```

We won't be strictly writing REST APIs, but it's good to know the name and the concept.

## HTTP Impedance Mismatch

HTTP has a lot of concepts that procedural programming languages do not: verbs, headers, paths.
Although they can map cleanly onto the idea of "values and function calls" that we've been using in JS and Python, they don't always.

So using an HTTP API from a procedural programming language requires fitting things together in custom ways.
Each API will do things slightly differently and there will be lots of edge cases for how you convert values and function calls back and forth.

## Native Wrappers

If an API is popular enough or from a big enough organization, sometimes there will be a very nice JS or Python wrapper around making manual HTTP calls.

```js
// Google Maps Interface
service = new google.maps.places.PlacesService(map);
service.getDetails(request, callback);
```

```py
# AWS Interface
import boto3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)
```

## API Keys

Most APIs have a concept called a **key**.
This is a unique identifier that allows the service to track who is making what kind of and how many calls.

You'll have to follow the service-specific instructions to register and send with every request your key.

**Never check in your keys.**
Follow my notes on [keeping secrets](/notes/secrets.md).
