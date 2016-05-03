# Constructors
Object methods allow you to specify an interface.
Then people can use your object without needing to write manipulation functions themselves.
This is the same reason that people write classes in Python.

JS gives you a way to do all of the setup of a _single instance_ of an object in a special function called a **constructor**.
It knows how to setup all of the properties on an instance from some parameters.
It is also given a special variable `this` that is the instance being prepared.
```js
function BankAccount(startingBalance) {
    this.balance = startingBalance;
    this.deposit = function (amount) {
        this.balance += amount;
    };
    // No return!
}
```
Constructor functions should always be named the type of object they are making in upper-case `CamelCase`.

To use the constructor, you have to call it with the keyword `new`.
The special naming is so you remember to call it with `new`.
```js
var davidsAccount = new BankAccount(0);
davidsAccount;  //> {"balance": 0, "deposit": function (amount) {...}}
var helensAccount = new BankAccount(100);
helensAccount;  //> {"balance": 100, "deposit": function (amount) {...}}
```
If you forget `new`, you don't get an error, unfortunately, you get `undefined` and pollute your global scope.

Once you've made your objects, you can use them!
```js
davidsAccount.balance;  //> 0
helensAccount.balance;  //> 100
davidsAccount.deposit(10);
helensAccount.deposit(20);
davidsAccount.balance;  //> 10
helensAccount.balance;  //> 120
```
