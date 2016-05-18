# Practice: Last Join
Make a function similar to `str.join(iter)` called `join_last(iter, joiner, last_joiner)`.

While `str.join(iter)` works like:
```python
', '.join(['apple', 'banana', 'mango'])  #> 'apple, banana, mango'
```

`join_last(iter, joiner, last_joiner)` will work like:
```python
join_last(['apple', 'banana', 'mango'], ', ', ', and')
#> 'apple, banana, and mango'
```
