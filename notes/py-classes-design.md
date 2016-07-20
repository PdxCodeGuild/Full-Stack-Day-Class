# Data Design

You now have a way of representing labeled, structured data in your programs.
This is very powerful.

Before, we could use tuples to represent structured data.
But we have to remember how things are stored in each tuple each time we use it.

```python
rain_measurements = [
    ("2016-01-01", 0.5),
    ("2016-01-02", 0.25),
    ("2016-01-03", 0.75),
]
for pair in rain_measurements:
    date, amount_inches = pair
```

Now, the data structure _documents itself_!
The fields are named and remind you how to use it at each point.

```python
class RainMeasurement:
    def __init__(self, date, amount_inches):
        self.date = date
        self.amount_inches = amount_inches

rain_measurements = [
    RainMeasurement("2016-01-01", 0.5),
    RainMeasurement("2016-01-02", 0.25),
    RainMeasurement("2016-01-03", 0.75),
]

for measurement in rain_measurements:
    measurement.date
    measurement.amount_inches
```

## Nested Structures

This is an especially powerful tool when you place instance of classes _within_ each other.

```py
class CodeGuildClass:
    def __init__(self, start_date, students):
        self.start_date = start_date
        self.students = students

class Student:
    def __init__(self, name):
        self.name = name

me = Student('David')
you = Student('Helen')
this_class = CodeGuildClass('2016-01-01', [me, you])

num_students = len(this_class.students)
num_students  #> 2
```

## Entity-Relation Diagrams

Use [entity-relation diagrams](/notes/entity-relation.md).
