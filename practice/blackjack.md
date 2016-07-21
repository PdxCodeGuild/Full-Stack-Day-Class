# Practice: Blackjack

Save your solution in a directory in `practice/` in a branch and make a GitHub pull request all named `blackjack`.

Let's start modeling a game of [blackjack](https://en.wikipedia.org/wiki/Blackjack).

Make a `Card` value class with a suit and a rank, both as strings, and a `Hand` value class with a list of cards.
In the `hand` module, implement top-level functions that:

* Add a card to a hand
* Score a hand
* Return if the score is over 21
* Allow a user to type in a hand and have it be converted into a `Hand` object

Make a `Deck` value class with a list of cards.
Initialize it with all cards in order.
In the `deck` module, implement top-level functions that

* Return a new deck that is shuffled
* Draw a card off the top of a deck
* Return if the deck is empty

Represent all cards in your program by _instance of the card_ class.
Don't use strings to represent a whole card like `'2H'` or something.

Write doctests for all of the functions.

## Scoring

Cards have integer point values.
Aces are 1 or 11, number cards are their number, face cards are all 10.
A hand is worth the sum of all the points of the cards in it.
An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.

## Advanced

*   Bring in your dealer hitting logic from the [21 practice problem](/practice/21.md) into a top-level function it's own module `dealer`.
    Update it to take in a `Hand` instance and return whether to hit.

*   Add a "card counting assistant" top-level function in a module `advisor`.
    Have it take in a deck and a hand and print out the probability that you will bust.
    You can find the [expectation value](http://www.wikihow.com/Calculate-an-Expected-Value) of the score of your hand given one more card; basically the sum of the probability of the card multiplied by the resulting score of the hand with that card.

*   Add in a UI so a single user can play versus the dealer.

*   Allow multiple hands to be played with the same deck.
