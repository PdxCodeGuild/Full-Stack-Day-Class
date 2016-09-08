# Catching Exceptions

You can **catch** exceptions using **try-except blocks**.
The code in the except block is only run if an exception is thrown.
Any code below where the exception is thrown is skipped over.

```py
try:
    x = int('hi')
    # This is skipped.
    x = 5
except ValueError:
    print('Error!')
    x = 4
print('Will print always. Error or not.')
x  #> 4
```

Program flow continues after the except block in every case.

Try to have your try blocks be as small as possible.
Almost every line could throw an exception, and if you "cast your net too wide", exceptions that represent bugs will be caught and make it harder to know what went wrong.

## Code Structure

Often you can prevent an exception from being thrown in the first place.
This technique is called **LBYL** or **Look Before You Leap**.

```py
word_to_count = {}
for word in words:
    if word not in counts:
        word_to_count[word] = 0
    word_to_count[word] += 1
```

You can also structure code that just handles the exception.
This technique is called **EAFP** or **Easier to Ask for Forgiveness than Permission**.

```py
word_to_count = {}
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1
```

I find EAFP code harder to understand, in general.
I would err on the side of finding a LBYL version.
