# Picking Data Structures

| Type  | Length? | Ordered? | Lookup? | Mutable? |
| ----- | ------- | -------- | ------- | -------- |
| List  | Yes     | Yes      | No      | Yes      |
| Dict  | Yes     | No       | Yes     | Yes      |
| Set   | Yes     | No       | No      | Yes      |
| Tuple | Yes     | Yes      | No      | No       |

There is _no shame_ in converting between data structures within a single problem.
There is no perfect data structure that answers all of your questions, so transform your data to a structure that lets you easily answer the question you're currently working on.

## Think Dict When

* Table
* Lookup
* Mapping
* Aggregation -- Dict of lists

## Think Set When

* Contains
* Unique
* Venn Diagrams
* "In this group not in that group"

## Think List When

* Order
* Queue
* Line
* Uniform interpretation
* "I have no idea" -- lists are a good default

## Think Tuple When

* Pair
* Different interpretations
* Has to be immutable for dict key
