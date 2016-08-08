# Constructors

JS gives you a way to do all of the setup of a _single instance_ of an object in a special function called a **constructor**.
It knows how to setup all of the properties on an instance from some parameters.
It is also has a special variable `this` in scope that is the instance being prepared.

```js
function BankAccount(startingBalance) {
  // `this` is an empty new object for you to setup.
  this.balance = startingBalance;
  this.deposit = function (amount) {
      // In this object method, `this` refers to the current object _at the call_.
      this.balance += amount;
  };
  // No return!
}
```

Constructor functions should always be named the type of object they are making in `WordCase`.

To use the constructor, you have to call it with the keyword `new`.
The special naming is so you remember to call it with `new`.

```js
var davidsAccount = new BankAccount(0);
davidsAccount;  //> {"balance": 0, "deposit": function (amount) {...}}
var helensAccount = new BankAccount(100);
helensAccount;  //> {"balance": 100, "deposit": function (amount) {...}}
```

If you forget `new`, you don't get an error, unfortunately.
The function returns `undefined` since it didn't have a return value.
Even worse, setting properties on `this` pollute your global scope.

If you use `this` outside of a constructor function, you don't get errors; `this` refers to the global scope.
Please never intentionally use it this way (no pun intended).

Once you've made your objects, you can use them!

```js
davidsAccount.balance;  //> 0
helensAccount.balance;  //> 100
davidsAccount.deposit(10);
helensAccount.deposit(20);
davidsAccount.balance;  //> 10
helensAccount.balance;  //> 120
```
