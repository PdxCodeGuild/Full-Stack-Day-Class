# Searching

**Searching** is looking through a dataset to find a _single value_ that matches some criteria.
There are a few totally different kinds of tasks that feel like "searching".

## Extrema

Looking for the "most" of a kind of value is actually a kind of [reduction](/notes/reducing.md).
Use [min()](https://docs.python.org/3/library/functions.html#min) and [max()](https://docs.python.org/3/library/functions.html#max), both with optionally the `key` keyword argument.
The `key` argument works with the same meaning as it does in [sorted()](/notes/sorting.md).

```py
heaviest_pumpkin = max(pumpkin_weights)
min_age = min(names, key=names_to_ages.get)
```

## Repeated Lookup

If you are repeatedly searching for a _single answer_ by equality, construct a dictionary with the **search key** as the dict key.
The search key is what you would check equality upon to know if you found the right thing.

This is basically a [mapping](/notes/mapping.md) with a dictionary in mind because it lets you do lookups very easily.

```py

contact_infos = [
    ('David', '503-555-9895', '123 Main St.'),
    ('Helen', '503-555-1234', '987 Ash St.'),
    ('Abby', '503-555-7777', '456 Water St.'),
]

phone_to_contact = {
    contact_info[1]: contact_info
    for contact_info
    in contact_infos
}
phone_to_contact['503-555-9895']
```

If there are multiple answers, this is a [grouping](/notes/grouping.md).

## Find First

The most general technique to find a _single item_ is to loop over all the input items in a function and return on one that matches.
You can use this technique when you have _complex matching criteria_.

Most of the time, you can use one of the other techniques.

```py
def find_prime(numbers):
    for num in nums:
        if is_prime(num):
            return num
```

If there are multiple answers, this is [filtering](/notes/filtering.md).
