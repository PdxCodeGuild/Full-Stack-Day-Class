# Advanced Variable Naming

Nested data structures add the following suggestions to our [original variable naming guidelines](/notes/naming-variables-basic.md).

## Mirror Data Structure

Have the name of the variable reflect the shape of the data.
Be _more descriptive_ than just adding `_dict` or `_list`.

*   For a dict, explain the keys and values.
    `product_to_price` is better than `prices`

*   For a list, use a plural of the contents.
    `friend_names` is better than `name_list`

*   For a set, comment on uniqueness.
    `uniq_words` is better than `words`
