# Generators and Yield

Anytime you're thinking about returning a list from a function, you could also "return" a generator.
It's effectively a much more flexible "list" where the output items are _calculated as needed_.

So instead of generating a list fully,

```py
def gen_odd_num(less_than):
    return [x for x in range(less_than) if x % 2 == 1]
```

you can **yield** out values.

```py
def gen_odd_num(less_than):
    for x in range(less_than):
        if x % 2 == 1:
            yield x
```

When the `yield` statement is run, the function pauses and actually _returns_!

```py
odd_nums = gen_odd_num(10)
odd_nums  #> <generator object gen_odd_num at 0x1097a1af0>
```

The return value is a **generator**.
It contains the yielded value and all of the "state" for that block of code to keep running from that point again.

Then the _calling_ code can process the item just yielded and when it's done it can tell the generator to resume work and generate a new value.
This is done through the **iterator protocol**.
Everything that has a `for` in it uses that.

```py
for x in odd_nums:
    print(x)  # 1 3 5 7 9
odd_nums = gen_odd_num(10)
for x in odd_nums:
    print(x)
```

A generator is not a list.
It does not implement most of the list operations.

```py
odd_nums[0]  # Throws TypeError
```

It also can only be _consumed once_.
For each time you iterate through it, you need to re-init the generator.
It only stores enough state to calculate the next value.

There is also a very concise form of making a generator function called a **generator expression**.
It looks like a list comprehension but is surrounded by parenthesis `()`.
It is _not_ a "tuple comprehension".

```py
odd_nums = (x for x in range(less_than) if x % 2 == 1)
odd_nums  #> <generator object <genexpr> at 0x109705ba0>
```

## Pipelines

Generators are especially great when you're stringing little steps of work on individual items together and you want some output immediately.

```py
def double_gen(iterator):
    for x in iterator:
        yield x * 2

def add_one_gen(iterator):
    for x in iterator:
        yield x + 1

def lookup_number_on_web_gen(iterator):
    for x in iterator:
        yield lookup_web(x)

# None of these calls calculates all results.
nums = range(100)
doubled_nums = double_gen(nums)
added_nums = add_one_gen(doubled_nums)
pipeline = lookup_number_on_web_gen(added_nums)
for web_data in pipeline:
    # Will start printing before all data is calculated.
    print(web_data)
```

## Design

Use generators when:

* Input data is huge
* You have many steps in a data transformation pipeline
* You want "progress" or some way to run code part of the way through working on inputs

## Crazy Talk

[Here](http://www.dabeaz.com/generators-uk/GeneratorsUK.pdf) is a talk on generators, yield, and **coroutines** which are a fun extension of the generator idea where data flows in both directions.
This is pretty heavy stuff but I think it's super cool.
Coroutines are the future of writing concurrent server code in Python.
