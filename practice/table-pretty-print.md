# Practice: Table Pretty Print

Save your solution as `practice/table-pretty-print.py`.

Write a program that reads a text file with the following format, but possibly with many more rows and / or columns.

```
Apple VW Oregon
Banana Ford Mississippi
...
```

Every line is a list of space-separated items.
All lines will have the same number of space-separated words on them.

Then your program will figure out how to pretty print a version of that table in the following format.

```
|-----|----|-----------|
|Apple|VW  |Oregon     |
|Pear |Ford|Mississippi|
|-----|----|-----------|
```

Each column has the width of the longest item.

## Advanced One

Modify your program to treat the first line as a header line.

The input will now look like:

```
Fruits Cars States
Apple VW Oregon
Banana Ford Mississippi
...
```

And the formatted output will now look like:

```
|------|----|-----------|
|Fruits|Cars|States     |
|------|----|-----------|
|Apple |VW  |Oregon     |
|Pear  |Ford|Mississippi|
|------|----|-----------|
```

## Super Advanced

*   Instead of hard coding a file name, have that file name come from the command line arguments given to the program.
    Cool! You've made your own command line tool that might come in handy.

*   Read the table from a CSV file using the standard library CSV parsing module.
