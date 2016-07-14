# Grouping

**Grouping** is re-structuring a collection so that items that _split into buckets_.
It is a kind of reduction.

E.g. Bucket a list of books by author.
Bucket names by what class list they appear in.

This is best done with _for loops_ and a _aggregating dict of lists_.

```py
my_books = [
    {'title': 'Moby Dick', 'author': 'Herman Melville'},
    {'title': 'Harry Potter', 'author': 'J. K. Rowling'},
    {'title': 'Bartleby', 'author': 'Herman Melville'},
]
author_to_books = {}
for book in my_books:
    if book['author'] not in author_to_books:
        author_to_books[book['author']] = []

    author_to_books[book['author']] += [book]
```
