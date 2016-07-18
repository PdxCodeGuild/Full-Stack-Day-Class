# Practice: Reviews

Save your solution as `practice/reviews.py`.

We're going to model a mini version of [Yelp](http://www.yelp.com/).
There are local business listings and users can post reviews, with a rating (1 - 5 points) and some text, of each business.

Write a program that will read a database of businesses, users, and reviews.

Businesses have:

* A name
* A location city

Users have:

* A name
* A hometown

Reviews have:

* The user name that wrote it
* The business name it is about
* A rating
* Some description text

Load in this data encoded in JSON format from these files.
Each line in these files is a single object of that kind.

* [Business Data](/practice/reviews-businesses.txt)
* [User Data](/practice/reviews-users.txt)
* [Review Data](/practice/reviews-reviews.txt)

Once you've done that, write out functions that answer the following questions each.

* Return all reviews for a single business
* Return the mean rating of a single business
* Return all reviews from a single user
* Return the mean rating of reviews from users from a given city

## Advanced

* Build a simple command line UI that invokes those functions
