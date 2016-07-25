# Type Interfaces

In addition to [encapsulation](/notes/py-classes-encapsulation.md), classes can also adhere to a **type interface**.
This is a set of functions and specifications of their behavior.
Any class that has implemented all of those functions can then be used in the same way.

Remember we've seen "list-like objects" or [sequences](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations)?
That was a formal lists of functions.

[Inheritance](/notes/py-classes-inheritance-basic.md) also defines an interface.
Any class that inherits from a base class will necessarily have all of the base class' functions.

This is where the [short form](/notes/py-type-methods-calling.md) of calling type methods is given power!
The long form means you have to know the _exact class type_ before calling, the short form let's Python figure it out!

You can use a variable assuming it adheres to an interface and not worry about the exact type of the person giving it to you.
You only care about the practical use.
