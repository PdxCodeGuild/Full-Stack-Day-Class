# Naming Functions

Similar suggestions apply for naming functions as [naming variables](/notes/naming-variables-basic.md), with a few additions.

## Use Parts of Speech

* Functions represent actions on data, so should be _verbs_ with _nouns_.

## Unambiguous

Try to think of all the other ways you could interpret the name you just came up with.
If other ways are wrong or misleading, try to be more specific.
Don't worry about long names;
it's better to be specific than short.

* `lookup_phone_number_by_name()` is better than `to_phone()`
* `prompt_for_command()` is better than `get_command()`

## Context

Also realize the context of your program to avoid needing longer names.

* `is_broken()` is fine instead of `is_link_broken()` if the topic of your program is just links
* `play()` is fine instead of `play_song()` if there's nothing else that could be played

## Parallel Construction

Your programs often have multiple related variables or functions, have the names show how they relate.

* `open_url_as_string()` and `open_url_as_file()` is better than `open()` and `open2()`

## Clarify Use

For function names, mention specifically what the arguments are and what the return value is, unless it's not obvious from the verb.

* `prompt_for_name()` is better than `prompt()`
* `invert_dict()` is better than `invert()`
* `open_url_as_string()` is better than `download()`

## Units

For numbers, don't assume the units are obvious.
They are required to use the number correctly!

* `subtract_time_seconds()` is better than `time_sub()`
