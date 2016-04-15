# Grouping
**Grouping** is re-structuring a collection so that items that _split into buckets_.
It is a kind of reduction.

E.g. Bucket a list of books by author.
Bucket names by what class list they appear in.

This is best done with _for loops_ and a _aggregating dict of lists_.
```python
my_books = [
    {'title': 'Moby Dick', 'author': 'Herman Melville'},
    {'title': 'Harry Potter', 'author': 'J. K. Rowling'},
    {'title': 'Bartleby', 'author': 'Herman Melville'},
]
my_books_by_author = {}
for book in my_books:
    if book['author'] not in my_books_by_author:
        my_books_by_author[book['author']] = []

    my_books_by_author[book['author']] += [book]
```
