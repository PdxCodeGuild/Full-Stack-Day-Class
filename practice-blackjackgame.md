# Practice: Blackjack Game
Implement playing a single hand of [blackjack](https://en.wikipedia.org/wiki/Blackjack) against a single computer dealer.

### Scoring
Cards have point values.
Aces are 1 or 11, number cards are their number, face cards are all 10.
A hand is worth the sum of all the points of the cards in it.
An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.

### Winning
The goal is to be the closest player to 21 points in your hand without going over.

### Play
Two cards are dealt to the player and the dealer.

The player goes first.
They can "hit" and get a new random card from the deck to increase the points in their hand.
If you hit and go over 21, you're out.
They can also "stand" and keep their current hand and end their turn.

Then the dealer plays identically.
The computer dealer will decide to hit if their current hand is less than 17 points;
they will stand otherwise.

### Step-by-Step
* Copy your blackjack hand scoring code.
* Make a class that represents a deck.
* Ensure that a deck is initialized with all of the cards.
* Add a function that removes and returns a random card from the deck.
* Implement the play above:
The user can decide whether to hit or stay.
The computer will play according to the dealer rules above.

## Advanced
* Allow multiple hands to be played with the same deck.
* Add a "card counting assistant".
When given the option to draw another card, print out the probability that your next card will keep you under 21.
