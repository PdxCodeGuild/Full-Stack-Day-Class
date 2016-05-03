# Prototypes
JS objects have a special concept called a **prototype**.
A child object **inherits** properties from its prototype object.

To give instances of an object a prototype, you set the `prototype` property _on the constructor_.
```js
function Cat() {
    this.noise = "Meow!";
}
Cat.prototype = {
    "noise": "Silent.",
    "paws": 4
};
```

Then when you make new instances using that constructor, missing properties will be found in the prototype.
```js
var elliot = new Cat();
elliot.noise;  //> "Meow!"
elliot.paws;  //> 4
```
