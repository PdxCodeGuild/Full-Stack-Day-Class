# Prototype Methods

Prototypes are especially powerful when combined with object methods to make **prototype methods**.
You can have some functions that work on lots of specific instances.

Within an object function, `this` always refers to the current object, even if it's made further up the prototype chain.

```js
var animalProto = {
    makeNoise: function() {
        return 'Says: ' + this.noise;
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
elliot.makeNoise();  //> 'Says: Meow!'
coltrain.makeNoise();  //> 'Says: Wolf!'
```

This is how all of those built-in methods on arrays and strings work.
