# Prototypes

JS objects have a special concept called a **prototype**.
A child object **inherits** missing properties from its prototype object.

You can use `Object.create(proto)` to make a new object with a given prototype object.

```js
var animalProto = {
    noise: 'Silent',
    paws: 4
};
var elliotCat = Object.create(animalProto);
elliotCat.noise = 'Meow!'
```

Note that giving `elliot` a `noise` property does not overwrite the prototype's properties.

```js
animalProto.noise;  //> 'Silent.'
elliotCat.noise;  //> 'Meow!'
elliotCat.paws;  //> 4
```

There is another, much more common, way to give an object a prototype.
You attach the prototype to the constructor function under the "magic" property `prototype`.

```js
function Cat() {
  this.noise = 'Meow!';
}
// Function's `.prototype` property is magic.
Cat.prototype = animalProto;

// When you use the function as a constructor, it will do the right thing.
milo = new Cat();
milo.paws;  //> 4
```

Note that the property lookup is **totally dynamic**.
If you modify the prototype after attaching it, the lookup still works.

```js
var animalProto = {
    noise: 'Silent',
    paws: 4
};
function Cat() {
  this.noise = 'Meow!';
}
Cat.prototype = animalProto;
milo = new Cat();
milo.poops;  //> undefined
// If we add new properties to the prototype, they are suddenly available on all objets that use it.
animalProto.poops = true;
milo.poops;  //> true
```

Prototypes themselves can have prototypes.
This linkage between prototypes is called the **prototype chain**.

```js
var mammalProto = {
  breathing: true
};
var catProto = Object.create(mammalProto);
catProto.paws = 4;
var elliot = Object.create(catProto);
elliot.breathing;  //> true
```
