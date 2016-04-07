## Joining
**Joining** is _following links_ between related data.
It might require aggregating along the way.

E.g. We have a list of books with authors, a list of authors with cities they live in, look up what books were written in a city.

This is best done with _lookup dicts_ that you've already made that group by what links you're using.
```python
book_data = [
    {'title': 'Moby Dick', 'author': 'Herman Melville'},
    {'title': 'Harry Potter', 'author': 'J. K. Rowling'},
    {'title': 'Bartleby', 'author': 'Herman Melville'},
]
author_data = [
    {'author': 'J. K. Rowling', 'city': 'London'},
    {'author': 'Herman Melville', 'city': 'New York City'},
]

city_to_authors = grouping_function_you_wrote(author_data)
author_to_books = grouping_function_you_wrote(book_data)

books_written_in_nyc = []
for author in city_to_authors['New York City']:
    books_written_in_nyc += author_to_books[author]
```
