# Practice: Visual Dice

Save your solution in a directory in `practice/` named `visual-dice`.
Your HTML file should be named `index.html`, your CSS file named `site.css`, and your JS file named `site.js` in that directory.

Give the user a number input box with a button "roll".
When they click that button, make that many 6-sided dice appear on the screen.

The dice should appear visually as dice, although for testing you can just start with numbers.
Come up with any reasonable way to display the visual dice.

If the user clicks any of the dice, it re-rolls just that one.
If they re-click the roll button, erase the dice and roll new ones.

At the bottom of the screen, show the sum of all the dice currently out.

## Advanced

Add a "number of sides" input box.
Change the "roll" button to a "add" button and a "reset" button.
"Add" when clicked will add that many new dice of that number of sides to the screen.
"Reset" will remove all dice.

They can still click on a die to re-roll it, but add a little "X" to delete that die.
Still show the sum.

## Super Advanced

Have your dice be rendered using `div`s with dot elements appropriately laid out for the number they're supposed to represent.
Use CSS animations to "roll" dice as they appear.
