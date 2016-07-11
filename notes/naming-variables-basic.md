# Naming Variables

Using good variable names means you'll have to think less about your code;
the names will remind you how to use each correctly.

Naming things is hard.
Don't be afraid to put in a **placeholder name** when you're first writing code.
But _always_ go back and fill in that placeholder with a good name when you understand its role.

There is no perfect name.
Names tradeoff between specificity, length, context, etc.

Try to use the following guidelines for helping you come up with good names.

## Use Parts of Speech

Variables represent data, so should be _nouns_.

* `found_name` is better than `found`

## Unambiguous

Try to think of all the other ways you could interpret the name you just came up with.
If other ways are wrong or misleading, try to be more specific.
Don't worry about long names;
it's better to be specific than short.

* `full_name` is better than `name`
* `word_without_punctuation` is better than `word`

## Context

Also realize the context of your program and current code section and use that to avoid needing longer names.

* `first` is fine instead of `first_name` if you're already only dealing with names
* `song` is fine instead of `playlist_song` if you're already only dealing with a single playlist

## Parallel Construction

Your programs often have multiple related variables or functions, have the names show how they relate.

* `all_phone_numbers` and `friend_phone_numbers` is better than `all_numbers` and `my_friend_phones`

## Units

For numbers, don't assume the units are obvious.
They are required to use the number correctly!

* `age_minutes` is better than `age`
* `distance_meters` is better than `distance`
