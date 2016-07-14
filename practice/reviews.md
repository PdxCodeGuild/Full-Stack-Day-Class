# Practice: Reviews

Save your solution as `practice/reviews.py` in a branch called `reviews` and make a GitHub pull request.

We're going to model a mini version of [Yelp](http://www.yelp.com/).
There are local business listings and users can post reviews, with a rating (1 - 5 points) and some text, of each business.

Copy and paste the following constant data at the top of your source.

```py
BUSINESS_DATA = [
  {'business_name': 'Dicks Burgers', 'Seattle'},
  {'business_name': 'Voodoo Donuts', 'city': 'Portland'},
]
USER_DATA = [
  {'user_name': 'Abby', 'hometown': 'Portland'},
  {'user_name': 'Helen', 'hometown': 'Portland'},
  {'user_name': 'Bobby', 'hometown': 'Chicago'},
  {'user_name': 'Carmen', 'hometown': 'Portland'},
]
REVIEW_DATA = [
  {'user_name': 'Abby', 'business_name': 'Dicks Burgers', 'rating': 5, 'text': 'Open late night!'},
  {'user_name': 'Bobby', 'business_name': 'Dicks Burgers', 'rating': 4, 'text': 'Super tasty, but such a long line!'},
  {'user_name': 'Carmen', 'business_name': 'Dicks Burgers', 'rating': 2, 'text': 'Gross meat.'},
  {'user_name': 'Helen', 'business_name': 'Voodoo Donuts', 'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
  {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts', 'rating': 5, 'text': 'Pink building is so cute!'},
  {'user_name': 'Abby', 'business_name': 'Voodoo Donuts', 'rating': 2, 'text': 'Diabetes inducing.'},
]
```

* Write a function that returns all reviews for a single business.
* Write a function that returns the mean rating of a single business.
* Write a function that returns all reviews from a single user.
* Write a function that returns the mean rating of reviews from users from Portland.
