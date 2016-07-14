# File IO

We need a way to read stored data.
The hard disk is the way a computer can persist data.
Python allows you to create **file objects** that represent files on the hard disk.

## Opening and Closing

Files are **opened** to read their contents.
That is done via the `open` function, which takes a file name and returns a file object.
File objects must be **closed** after you're done using them.

To do that you use a **with assignment**.
A with assignment takes the file object that must be closed, then `as`, then a variable name to assign the file object to, then runs a block.
When the block ends, the file object is closed, so all operations that use the file object must be in the block.
Don't use the variable name after the block.

```py
with open('phonebook.txt') as phone_book_file:
    book_lines = phone_book_file.readlines()

do_something_with(book_lines)
```

File names are relative to the working directory the program is in.

## Reading

Let's assume we've already opened a file `f` and are inside a `with` block.
You can use the following operations while the file is open.

To get all lines as a list of strings:

```py
f.readlines()  #> ['First line\n', 'Second line\n']
```

Lines include the newline character, which is represented in strings by `"\n"`.

To perform a block on each line of a file, you can use a `for` loop over the file object:

```py
for line in f:
  do_something_with(line)
```

## Writing

File objects have to be explicitly opened for writing, otherwise the following methods error.
To open a file object for writing, you give `open` a second parameter as a string.
If that parameter is `'w'`, it will allow writing;
it will also erase the contents of any file at that file name.

```py
with open('phonebook.txt', 'w') as phone_book_file:
  write_things_to(phone_book_file)
```

The one function to write takes in a string to write:

```py
f.write('A line to write\n')
```

That string must include newline characters if you want to have the text appear on separate lines.

## Example

Write a phonebook file:

```py
phonebook = {'David': '5551234', 'Alice': '6662345'}
with open('phonebook.txt', 'w') as phone_book_file:
  for name, number in phonebook.items():
    line = '{} {}\n'.format(name, number)
    phone_book_file.write(line)
```

Read a phonebook file:

```py
with open('phonebook.txt') as phone_book_file:
  data_in_phonebook = phone_book_file.readlines()

for line in data_in_phonebook:
  name, number = line.strip().split()
  print("{} - {}".format(name, number))
```
