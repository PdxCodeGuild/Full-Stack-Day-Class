# Practice: Taxes

Save your solution in a Python file in `practice/` in a branch and make a GitHub pull request all named `taxes`.

Income tax in Oregon is **progressive**.
That means the more you make, the larger fraction of that _additional_ income you pay.

The tax brackets in 2014 were:

* First $3,350 of income is taxed at 5%
* The next $5,050 is taxed at 7%
* The next $116,000 is taxed at 9%
* Any more income is taxed at 9.9%

Someone who earns $50,000 this year pays:

* 5% of their first $3,350 in income -- $167.50
* 7% of their next $5,050 in income -- $353.50
* 9% of their next $116,600 in income (which is only $50,000 - $5,050 - $3,350 = $41,600) -- $3,744

So $167.50 + $353.50 + $3,744 or $4,265 total.

Write a program that let's someone enter their income and calculates and prints their total Oregon income tax.

Start with a tax burden of $0 and "taxable income" of the full income entered.
Then go through each tax bracket in increasing order, calculating how much of the remaining taxable income is in the bracket, adding the tax burden due to that bracket, and reducing the remaining amount of taxable income.
Go until there's no income left or you reach the biggest tax bracket.

## Super Advanced

Modify your code to allow someone to specify arbitrary tax brackets in code and still calculate the total tax burden.

```py
brackets = [
    (3350, 0.05),
    (5050, 0.07),
    (116600, 0.09),
    (None, 0.099),
]
```
