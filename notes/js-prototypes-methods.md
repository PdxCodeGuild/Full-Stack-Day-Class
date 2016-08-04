# Prototype Methods

Prototypes are especially powerful when combined with object methods to make **prototype methods**.
You can have some functions that work on lots of specific instances.

```js
var animalProto = {
    makeNoise: function() {
        return this.noise;
    }
};

function Cat() {
    this.noise = 'Meow!';
}
Cat.prototype = animalProto;

function Dog() {
    this.noise = 'Wolf!';
}
Dog.prototype = animalProto;

var elliot = new Cat();
var coltrain = new Dog();
elliot.makeNoise();  //> "Meow!"
coltrain.makeNoise();  //> "Wolf!"
```

This is how JS implements things like Python's type methods.
JS arrays, strings, numbers all have prototype methods as a sort of "standard library".

As a crash course, here are the prototype methods for [strings](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#Methods_2) and  [arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array#Methods_2).
You can look at the [full reference for all types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference).

Many of these prototype methods are replicated in [Lodash](/notes/js-lodash.md).
I encourage you to use the Lodash versions, they often have cleaner semantics.
