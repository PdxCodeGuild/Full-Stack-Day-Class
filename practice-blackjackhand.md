# Practice: Blackjack Hand
Implement _just scoring_ a single hand of [blackjack](https://en.wikipedia.org/wiki/Blackjack).
Don't worry about modeling a deck or a game yet.

* Make a class that represents a card with a suit and a rank.
* Make a class that represents a hand with a list of cards.
* Add functions that adds a card to a hand, one that scores a hand, and one that returns if the score is over 21.
* Test out your classes and functions by constructing instances in code from literals. E.g. Make the jack of diamonds.
* Allow a user to type in a hand and have it be converted into card objects and then scored.

Represent all cards in your program by _instance of the card_ class.
Don't use strings to represent a whole card like `'2H'` or something.

## Scoring
Cards have integer point values.
Aces are 1 or 11, number cards are their number, face cards are all 10.
A hand is worth the sum of all the points of the cards in it.
An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.
