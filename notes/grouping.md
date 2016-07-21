# Grouping

**Grouping** is re-structuring a collection so that items that _split into buckets_.
It is a kind of [reduction](/notes/reducing.md).

E.g. Bucket a list of books by author.
Bucket names by what class list they appear in.

This is best done with `itertools.groupby()`.
Check out the [documentation](https://docs.python.org/3/library/itertools.html#itertools.groupby) for it.

1. Determine what your input list or sequence is.
1. Write a function that takes in one item from the input and returns what group to put it in, called a **grouping key**.
1. Call `groupby()` and do some simple conversion to a dict of lists. (It actually returns nested iterators.)

```py
from itertools import groupby

my_books = [
    {'title': 'Moby Dick', 'author': 'Herman Melville'},
    {'title': 'Harry Potter', 'author': 'J. K. Rowling'},
    {'title': 'Bartleby', 'author': 'Herman Melville'},
]

# 2. Calculate Grouping Key
def get_author(book):
    return book['author']

# 3. Call and Convert
author_to_books = {
    group_key: list(grouped_items)
    for group_key, grouped_items
    # 1. Specify Input
    in groupby(my_books, get_author)
}
author_to_books  #> {'Herman Melville': [{'title': 'Moby Dick', 'author': 'Herman Melville'}, {'title': 'Bartleby', 'author': 'Herman Melville'}], 'J. K. Rowling': [{'title': 'Harry Potter', 'author': 'J. K. Rowling'}]}
```

Note that if your final goal is groups of some derived value (and not the input items themselves), do a [mapping](/notes/mapping.md) after the reduction.

```py
author_to_titles = {
    author: [book['title'] for book in books]
    for author, books
    in author_to_books
}
author_to_titles  #> {'Herman Melville': ['Moby Dick', 'Bartleby'], 'J. K. Rowling': ['Harry Potter']}
```

If you don't want to have to remember to do all the casting on the result, copy and paste this function into your code.

```py
from itertools import groupby

def group_by(iterable, key):
    """Place each item in iterable into a bucket based on the calling the key
    function on the item.
    """
    return {group: list(items) for group, items in groupby(iterable, key)}
```
