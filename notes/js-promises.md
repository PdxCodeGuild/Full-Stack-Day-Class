# Promises

JavaScript is single threaded.
It can only do one thing at a time.
If JS is waiting for something to complete, it **blocks** or can't do anything else in the mean time.

```js
$('button').on('click', function() {
  // Browser is unresponsive while running this whole function when a click happens.
  var result = slowDownloadContent();
  var transformedResult = fastTransformResult(result);
  fastUpdateUI(transformedResult);
});
```

Up until this point, we didn't really deal with anything "slow".
Going out to the network and fetching some new content is relatively slow.
If we want to enable our JS to do exciting things like that, we need a model that allows it.

A **promise** is an object that _will_ contain a useful value, but doesn't yet.
An "empty" promise is **pending**.
A promise that found a good value is called **fulfilled**.
If you give a function to `then()` it will be called when fulfilled.

They are also written in a method chaining style.

```js
$('button').on('click', function() {
  // This click function finishes fast!
  // All it does is remember what it should go back to doing when the value has arrived.
  downloadContentPromise().
    then(function(result) {
      // This only runs once the promise is fulfilled.
      var transformedResult = fastTransformResult(result);
      fastUpdateUI(transformedResult);
    });
});
```

But what if you have multiple slow steps that depend on each other?
Any then function that returns a promise will be passed into the next then function only when it's done!

```js
$('button').on('click', function() {
  downloadContentPromise().
    // If a "then" function returns a value or a promise, the resolved value is passed along!
    // This allows you to string together slow operations and only run the next step once the previous is done.
    then(function(result) { return slowTransformResultPromise(result); }).
    then(function(transformedResult) { fastUpdateUI(transformedResult); });
});
```

Both of those then anonymous functions are effectively identity functions, so they could be replaced with the inner function name.

```js
$('button').on('click', function() {
  // This click function finishes fast!
  // All it does is remember what it should go back to doing when the value has arrived.
  downloadContentPromise().
    then(slowTransformResultPromise).
    then(fastUpdateUI);
});
```

Promises also allow for failure and no normal return value.
A failed promise is called **rejected**.
If you give a function to `catch()`, it will be only called upon rejection.
The rejection can also include an error object.

```js
$('button').on('click', function() {
  // This click function finishes fast!
  // All it does is remember what it should go back to doing when the value has arrived.
  downloadContentPromise().
    then(slowTransformResultPromise).
    catch(function(error) { updateErrorMessage(error); }).
    then(fastUpdateUI);
});
```

There is [this pretty great article](http://www.html5rocks.com/en/tutorials/es6/promises/) about JS promises and some JS promise [API documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).
