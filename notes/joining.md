# Joining

**Joining** is _following links_ between related data to produce derived groups.

E.g. We have a list of books with authors, a list of authors with cities they live in, look up what books were written in a city.

This is best done by [mapping](/notes/mapping.md) into _lookup dicts_ then further [grouping](/notes/grouping.md) on those lookup dicts.

1.  Generate lookup dicts that will link between the data you want to join.
    This is made super easy if you name your dicts like `x_to_y` and `y_to_z` because then you can follow from `x` to `z`.

1.  Write a grouping key function.
    It will take in your items you want to be grouping and use a daisy chain of lookup dicts to find the derived value you want to group upon.

1.  Perform a grouping using that function.

```py
book_data = [
    {'title': 'Moby Dick', 'author': 'Herman Melville'},
    {'title': 'Harry Potter', 'author': 'J. K. Rowling'},
    {'title': 'Bartleby', 'author': 'Herman Melville'},
]
author_data = [
    {'name': 'J. K. Rowling', 'city': 'London'},
    {'name': 'Herman Melville', 'city': 'New York City'},
]

# 1. Setup All Lookup Dicts
author_name_to_city = {
    author['name']: author['city']
    for author
    in author_data
}

# 2. Write Grouping Key Function
def get_city_for_book(book):
    return author_to_city[book['author']]

# 3. Group Requested Items
city_to_books = {
    city: list(books)
    for city, books
    in groupby(book_data, get_city_for_book)
}
```
