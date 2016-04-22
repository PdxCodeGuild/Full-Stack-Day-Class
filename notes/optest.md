# Order of Operations Tests

```python
print([sorted('apple')[-2]])
```

```python
x = 'y'
y = 'x'
print({x: 'y', y: x}['x'])
```

```python
x = set('apple')
print([4 > 5, 6 > 7, 9 > 8][-1] and 'ap' in x)
```

```python
print(list('apple').index(max('apple')))
```

```python
print(all([x in 'apple' or x in 'pear' for x in 'repl']))
```

```python
print('?'.join(list(zip(['1', '2', '3'][1:], {'a': 5, 'b': 6}))[-2]))
```

```python
x = ['a', 'b', 'c']
print([x[1].join((str(y[0]), y[1])) for y in enumerate(x)][1])
```

```python
x = ['a', 'b', 'c']
y = [1, 2, 3, 4]
z = [i[1] % 2 == 0 for i in zip(x, y)]
print(list(reversed(z))[0])
```

```python
x = [1, 2, 3]
d = 'p-'
print('apple-orange'[x[x[x[0]]]:9].split(d[x[1]-3])[min(x)][1:x[2]])
```

```py
print(sum([sum(range(i)) for i in range(10) if i in (5, 7)]))
```
