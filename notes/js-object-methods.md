# Object Methods

JS allows you to attach functions _to objects_.
Functions are just values, so they can be assigned to properties just like any other value, resulting in an **object method**.

```js
var animalNoises = {
  makeDogNoise: function() {
    return 'Woof!';
  },
  makeCatNoise: function() {
    return "Meow!";
  },
};
animalNoises.makeDogNoise();  //> 'Woof!'
animalNoises.makeCatNoise();  //> 'Meow!'
```

These object methods have a superpower!
They can modify the _other properties_ of that object.

When this function runs, it a special variable `this` is in scope.
`this` references the object instance the function is attached to!
It's like `self` in Python, but isn't passed in explicitly.

So you can do things like:

```js
var davidsBankAccount = {
  balance: 20,
  deposit: function(amount) {
    this.balance += amount;
  }
};
davidsBankAccount.balance;  //> 20
davidsBankAccount.deposit(100);
davidsBankAccount.balance;  //> 120
```
