# Naming Things
Using good variable and function names means you'll have to think less about your code;
the names will remind you how to use each correctly.

Naming things is hard.
Don't be afraid to put in a **placeholder name** when you're first writing code.
But _always_ go back and fill in that placeholder with a good name when you understand its role.

There is no perfect name.
Names tradeoff between specificity, length, context, etc.

Try to use the following guidelines for helping you come up with good names.

## Use Parts of Speech
* Variables represent data, so should be _nouns_.
* Functions represent actions on data, so should be _verbs_ with _nouns_.

## Unambiguous
Try to think of all the other ways you could interpret the name you just came up with.
If other ways are wrong or misleading, try to be more specific.
Don't worry about long names;
it's better to be specific than short.

* `full_name` is better than `name`
* `lookup_phone_number_by_name()` is better than `to_phone()`
* `word_without_punctuation` is better than `word`
* `prompt_for_command()` is better than `get_command()`

## Mirror Data Structure
Have the name of the variable reflect the shape of the data.
Be more descriptive than just adding `_dict` or `_list`.

* For a dict, explain the keys and values.
`product_to_price` is better than `prices`
* For a list, use a plural of the contents.
`friend_names` is better than `name_list`
* For a set, comment on uniqueness.
`uniq_words` is better than `words`

## Parallel Construction
Your programs often have multiple related variables or functions, have the names show how they relate.

* `open_url_as_string()` and `open_url_as_file()` is better than `open()` and `open2()`
* `all_phone_numbers` and `friend_phone_numbers` is better than `all_numbers` and `my_friend_phones`

## Clarify Use
For function names, mention specifically what the arguments are and what the return value is, unless it's not obvious from the verb.

* `prompt_for_name()` is better than `prompt()`
* `invert_dict()` is better than `invert()`
* `open_url_as_string()` is better than `download()`

## Units
For numbers, don't assume the units are obvious.
They are required to use the number correctly!

* `age_minutes` is better than `age`
* `distance_meters` is better than `distance`
* `time_difference_seconds()` is better than `time_sub()`
