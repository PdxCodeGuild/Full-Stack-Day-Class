# Entity-Relation Diagrams

**Entity-relation diagrams** are a way of visually mapping out the nouns in your project and figuring out your data model.

Think of every top-level noun.
That is an **entity**.
Make a _box_ with that title.
Then think of all of the things you have to remember about it.
Those are the **fields** of an entity.
_List_ all those things in that box.

If they're simple things, they can be just a field.

If there are complex things, they should be another entity.
Those two entities then have a **relationship**.
Draw a line connecting the containing **parent entity** to the dependent **child entity**.

There are a few types of relationships.

## One-to-One

**One-to-one** relations are when the entities come in pairs.
Draw a line from the field in the parent entity to the child entity.

E.g. Every person has one resume and every resume has one person.

## One-to-Many

**One-to-many** relations are when the parent entity has multiple, _globally unique_ child entities.
Draw a line from the field in the parent entity to the child entity that ends in multiple connections.

E.g. A playlist has multiple entries.

## Many-to-Many

**Many-to-many** relations are entities are connected together in a graph or network, or a parent entity has multiple, _globally non-unique_ child entities.

E.g. Facebook.
Each book can have multiple authors and authors can write multiple books.
