# Sequence Operators

All sequences, like strings and lists, have a few useful operators.

## Length

Many sequences have a **length**.
You can use the built-in function `len()` to get it.

```py
name = 'David'
len(name)  #> 5
names = ['David', 'Helen']
len(names)  #> 2
```

## Indexing and Slicing

Sequences have the **subscript operator** or **get operator**, `[]`.
It returns the value contained at a numbered position in the sequence, called an **index**.
In Python, all sequences start counting from _zero_.
If you attempt to access an index that doesn't exist, an `IndexError` is thrown.

```py
name = 'David'
ages = [5, 10, 15]
name[0]  #> 'D'
name[4]  #> 'd'
name[10]  # Throws IndexError
ages[1]  #> 10
```

Most sequences support **negative indices** which count backwards from the end of sequence.

```py
name[-1]  #> 'd'
name[-3]  #> 'v'
ages[-1]  #> 15
```

You can also use the subscript operator to **slice** a sequence, or get part of it.
Pass a starting index, then a colon `:`, then an _exclusive_ ending index.
If you leave out a starting or ending index, it defaults to the beginning or end of the sequence, respectively.

```py
name[2:4]  #> 'vi'
name[:4]  #> 'Davi'
name[2:]  #> 'vid'
ages[1:]  #> [10, 15]
```

Remember, `[]` is just an operator that returns a value, so you can put them anywhere an expression is needed.

```py
x = [[1, 2], [3, 4]]
x[1][0]  #> 3
['a', 'b', 'c'][[1, 2, 3][1]]  #> 'c'
```

## Concatenation

Sequences can be **concatenated** in order by using plus `+`.

```py
[1, 2] + [3]  #> [1, 2 ,3]
'Hello, ' + 'David'  #> 'Hello, David'
```

## In Operator

You can test if a single inner value exists in a sequence by using the `in` operator.
It only checks single values and containment at the _top level_.

```py
4 in [2, 4, 6]  #> True
'v' in 'David'  #> True
'v' in ['David']  #> False
[2, 4] in [2, 4, 6]  #> False
```
