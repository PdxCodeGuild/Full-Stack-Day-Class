# Garbage Collection

Python stores all data as objects in memory.
Computer memory can be thought of as a giant table.
You can put an object in each table cell.

To actually look up some data, you have to remember which cell it's in.
Variables hold these **references** to locations or **addresses** in the table.

| Address | Data  |
| ------- | ----- |
| 1       |       |
| 2       |       |
| 3       | `Hi!` |
| 4       |       |
| 5       | 45    |
| 6       |       |

| Variable | Address |
| -------- | ------- |
| `greet`  | 3       |
| `age`    | 5       |

All of your code is flinging references around and giving them different labels.
Most code transforms some data through a series of steps, then returns a distilled result.

```py
age = 30
next_age = age + 1
# Is `age` ever used again? Do we have to remember it?
```

Your web servers are constantly performing little operations to return pages and running for days at a time.
Computers only have a finite amount of memory, so how do we reclaim unused data table cells?
That process is called **garbage collection**.

Python uses a combination of two techniques to collect garbage.

## Reference Counting

The first is called **reference counting**.
Python, internally, keeps track of how many variables hold references to some data cell.
That is called the **reference count of an object**.

| Address | Data  | Reference Count |
| ------- | ----- | --------------- |
| 1       |       |                 |
| 2       |       |                 |
| 3       | `Hi!` | 1               |
| 4       |       |                 |
| 5       | 45    | 2               |
| 6       |       |                 |

Whenever syntactically a value is assigned to a new slot, it's reference count is incremented.

```py
names = ['David']  # +1, 1
my_names = names  # +1, 2
return my_names  # +1, 3
```

Whenever a variable falls out of scope, its reference count is decremented.

```py
def f(x, y):
    s = sum(x, y)
    return s
    # x, y: -1
```

Whenever a reference count reaches zero, you know a data cell is unused and can be erased and marked for re-use.
You can deterministically check this whenever you decrement a reference count.

Reference counting is great.
It has low, fixed memory cost (storing those counts) and a low, fixed time cost (incrementing and decrementing those counts).

But!
It has one downside.
Cyclical structures never get to reference count zero and deallocated.
They exist as little "islands" of objects.

```py
one = {'friend': None}  # Call this value A. A +1, RC 1
two = {'friend': one}  # Call this value B. B +1, RC 1; A +1, RC 2
one['friend'] = two  # B +1, RC 2
# Both one and two fall out of scope. A -1, RC 1; B -1, RC 1
# But neither are at zero, even if never referenced anywhere else!
```

This is a contrived example, but in lots of Python code there are subtle cycles.

## Mark and Sweep

Because of this, there needs to be another step on the garbage collection process to remove those cycle islands.

Python also has a list of all global, top level references.
Periodically, it makes a copy of all the reference counts, goes through every object referred to them in a nested way, and removes all internal references from the reference counts.
This will cause all cycles to go to zero!

This is great, but requires a lot of work.
You have to walk the **object graph** and see which things actually refer to each other.
Also, while you're doing this, you can't be changing the object graph!
So the program has to _stop running_.
These **garbage collection pauses** suck, but you don't have to do them all that often, just when you're running out of memory, or when you know you won't mind having the program pause.

## Manual Memory Management

Do we have to deal with all this?
No.
Some programming languages don't have memory management, like C and C++.
You have to explicitly annotate your code to **allocate** and **free** values.

```c
t_contact_info *contact_info = (t_contact_info *) malloc(sizeof(t_contact_info));
free(contact_info);
```

This sucks.
You have to manually work out in your head all of the situations in which a reference might be saved and handle them.

It's hard to tell when you got this wrong sometimes because the address that used to contain valid data, might be re-used with valid data!
Or not be cleared for performance reasons!

Many years of work on bug fixes and security holes have come about because of having to manually manage memory.

It sucks so much, no one even thinks about making programming languages any more in which you have to do this all by hand.

## Further Reading

This is a huge area.
There is a tradeoff between data model flexibility, excess computer work, and excess programmer work that is still being explored.

Here are a few more articles that discuss the garbage collection and other memory management ideas:

* [Visualizing Garbage Collection in Ruby and Python](http://patshaughnessy.net/2013/10/24/visualizing-garbage-collection-in-ruby-and-python)
* [How does garbage collection in Python work?](https://www.quora.com/How-does-garbage-collection-in-Python-work)
* [Java Garbage Collection](http://www.oracle.com/webfolder/technetwork/tutorials/obe/java/gc01/index.html)
* [Swift Automatic Reference Counting](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/AutomaticReferenceCounting.html)
* [Rust Ownership](https://doc.rust-lang.org/book/ownership.html)
