# App Requirements

In order for you to have saved a full definition of your application, you need to have saved all of the specific versions of each dependency.
Instead of committing the source of the dependencies, we save a list of their names and version numbers in `requirements.txt`.

It is a text file with one dependency on each line.

```
requests==2.10.0
Pillow==3.1.0
```

In general, you will be generating this file via [freezing your virtualenv](/notes/py-virtualenv.md#freeze).
