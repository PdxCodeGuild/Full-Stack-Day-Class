# Practice: Restaurant Reviews
We're going to model a mini version of [Yelp](http://www.yelp.com/).
There are local business listings and users can post reviews, with a rating (1 - 5 points) and some text, of each business.

* Make a `user_name` class: it will have "user name" and "hometown" field.
* Make a `Business` class: it will have "name" and "city" field.
* Make a `Review` class: it will have "user name", "business name", "rating", and "review text" fields.
* Create a list `businesses` with all instances of the Business class, a list `users` with all instances of the User class, and a list `reviews` with all instances of the Review class.
Load the following data into instances and put in those lists:
```python
raw_business_data = [
  {'business_name': 'Dicks Burgers', 'Seattle'},
  {'business_name': 'Voodoo Donuts', 'city': 'Portland'},
]
raw_user_data = [
  {'user_name': 'Abby', 'hometown': 'Portland'},
  {'user_name': 'Helen', 'hometown': 'Portland'},
  {'user_name': 'Bobby', 'hometown': 'Chicago'},
  {'user_name': 'Carmen', 'hometown': 'Portland'},
]
raw_review_data = [
  {'user_name': 'Abby', 'business_name': 'Dicks Burgers', 'rating': 5, 'text': 'Open late night!'},
  {'user_name': 'Bobby', 'business_name': 'Dicks Burgers', 'rating': 4, 'text': 'Super tasty, but such a long line!'},
  {'user_name': 'Carmen', 'business_name': 'Dicks Burgers', 'rating': 2, 'text': 'Gross meat.'},
  {'user_name': 'Helen', 'business_name': 'Voodoo Donuts', 'rating': 1, 'text': 'I do not like bubblegum on my donuts.'},
  {'user_name': 'Bobby', 'business_name': 'Voodoo Donuts', 'rating': 5, 'text': 'Pink building is so cute!'},
  {'user_name': 'Abby', 'business_name': 'Voodoo Donuts', 'rating': 2, 'text': 'Diabetes inducing.'},
]
```

Now, don't use these dicts or lists for any further operations.

* Write a function that returns all reviews for a single business.
* Write a function that returns the mean rating of a single business.
* Write a function that returns all reviews from a single user.
* Write a function that returns the mean rating of reviews from users from Portland.
