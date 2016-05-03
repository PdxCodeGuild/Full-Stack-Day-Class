# Prototypes
JS objects have a special concept called a **prototype**.
A child object **inherits** missing properties from its prototype object.

You can use `Object.create(proto)` to make a new object with a given prototype object.
```js
var proto = {
    noise: 'Silent',
    paws: 4
};
var elliot = Object.create(proto);
elliot.noise = 'Meow!'
```

Note that giving `elliot` a `noise` property does not overwrite the prototype's properties.
```js
proto.noise;  //> 'Silent.'
elliot.noise;  //> 'Meow!'
elliot.paws;  //> 4
```
