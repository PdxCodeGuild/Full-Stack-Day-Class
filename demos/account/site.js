'use strict';

var davidsAccount = {
  balance: 0,
  // Functions are just values and can be put on objects.
  /**
   * Deposit an amount to an account in-place.
   */
  deposit: function(amount) {
    // Inside of a function attached to an object `this` is magically the instance it is attached to.
    this.balance += amount;
  }
};

console.log(davidsAccount.balance);  //> 0
davidsAccount.deposit(50);
console.log(davidsAccount.balance);  //> 50

// Can make prototypes, which hold all shared functions or data.
var accountPrototype = {
  /**
   * Deposit an amount to an account in-place.
   */
  deposit: function(amount) {
    // Object function is currently attached to.
    this.balance += amount;
  }
};

/**
 * Creates a bank account with a balance and deposit function.
 */
function BankAccount(balance) {
  // Inside of a constructor function, `this` is magically the new empty object you need to setup.
  this.balance = balance;
  // Don't return!
}
// Cause all new objects made with this constructor to have a prototype.
BankAccount.prototype = accountPrototype;

// ALWAYS CALL CONSTRUCTOR FUNCTIONS WITH `new`.
// This ensures `this` is setup correctly.
// You won't get an error if your forget, just `undefined`.
var helensAccount = new BankAccount(80);
console.log(helensAccount.balance);  //> 80
helensAccount.deposit(40);
console.log(helensAccount.balance);  //> 120

// Prototype lookup is totally dynamic.
// If you add things to the prototype, they appear on all objects using it!
helensAccount.withdraw(100);  // TypeError
/**
 * Withdraw an amount from an account in-place.
 */
accountPrototype.withdraw = function(amount) {
  this.balance -= amount;
};
helensAccount.withdraw(100);
console.log(helensAccount.balance);  //> 20
