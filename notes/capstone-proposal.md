# Capstone Proposal

Write up a **proposal** for your [MVP](/notes/capstone-mvp.md) capstone project idea.
It should be _brief_ and clear single text document that follows the rubric below of no more than two pages.
Feel free to hand draw mockups and include them if that helps you plan, but they can't take the place of a write-up.

Your proposal serves a few important purposes:

1.  Front-load decision making.
    Figure out _now_ how you're going to solve your problems.
    Do some prototyping and research.

1.  Guidance _for you_.
    When you're working on the project, you can look at it and know what to do next.

1.  Safety check that it meets the requirements below.
    I am _not_ evaluating the business savvy of your project (although I'd be happy to give my two cents, if you ask).

## Requirements

Your capstone proposal must:

* Follow the rubric
* Be plain text or Markdown
* Describe a [MVP](/notes/capstone-mvp.md) that meets [the capstone requirements](/notes/capstone-intro.md#requirements)
* Describe a project that you can finish in time
* Be kept up-to-date as your project expands or evolves

## Rubric

Please address all of the following areas in your proposal **for just your MVP**.
Even if you have grand dreams for working on your capstone full-time, _only_ write up the MVP here.

### Name

Give your product or project a simple, short name.

### Product Overview

What is your MVP web app going to do?
How does a user interact with it on a high level?

### Specific Functionality

Spend some time drawing out on paper mockups _every_ page of your MVP site.
Annotate _every_ component of the interface _every_ action the user can take.

If there is any actions your app needs to take in the background describe _each_ of them and how they change the underlying data your app saves.

**Pick the minimum feature set for your product to work.**
Everything else should go in the "further work" section.

You don't have to submit the mockup drawings, but do write out a description of _every_ page and component and action.
I literally mean _every_.

### Data Model

What are the persistent "nouns" you need to save across pages in your project MVP?
What do they represent?

We'll be using a relational database which models things like a spreadsheet.
There are fixed fields and every instance

How do you need to _search_ for specific instances of nouns?

### Technical Components

What are the "moving parts" of your MVP?
What are the things like "modules" you're going to write?
How do they talk to each other?

_Make decisions_ here and now.
Do research and prototyping to figure out what libraries and technologies will help you solve your problems.
Write up which ones you'll use.
It's okay if they end up not working and you have to change your plans.

This is _more specific_ than "Django backend, CSS style, etc."
Please specify what specific technical problems you'll have to solve and a guess at the solution.

### Schedule

Write out the order in which you will tackle your technical components of your MVP.

What are the easy parts?
What are the hard parts?
Can you guess how long you'll take for each?

Work on the tough and crucial parts first.

### Further Work

All of the above parts are _just addressing your MVP_.
Here you should outline other features you'd like to implement if you get "done" early.
Order them by importance towards your high-level goal and what order you'll work on them later.

Don't work on any of these features until **all of MVP is complete**.

## Submission

Create a _new_ git repo based on your project name [in GitHub](https://github.com/new).
Init that repository with a readme.
Write up your proposal as `proposal.md` and link to it from the readme.
I don't care that you learn all of the fancy parts of [writing Markdown documentation](https://help.github.com/articles/basic-writing-and-formatting-syntax/), but just get some basic sections that follow the rubric above.

Email me the URL to your capstone repo on GitHub before the proposal is due.
