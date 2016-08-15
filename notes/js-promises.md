# Promises

JavaScript is single threaded.
It can only do one thing at a time.
If JS is waiting for something to complete, it **blocks** or can't do anything else in the mean time.

```js
$('button').on('click', function() {
  // Browser content is unresponsive while running this whole function when a click happens.
  var result = slowDownloadContent();
  var transformedResult = fastTransformResult(result);
  fastUpdateUI(transformedResult);
});
```

Up until this point, we didn't really deal with anything "slow".
Going out to the network and fetching some new content is relatively slow.
People perceive something as "instantaneous" if it happens within 200ms.
If we want to enable our JS to do exciting things like that, we need an **asynchronous** model that allows it.

The biggest source of "slow" things is waiting on network IO.
Network IO is a convenient case where adding in simple event handling concurrency will work.

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

But what if you have multiple slow requests that depend on each other?
We could be calling out to another network service with the result.
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

## Callbacks

You have also encountered another way of doing asynchronous coding.
For events, you registered callbacks.
Other "slow" code can also be made asynchronous by introducing callbacks.

The example above, if written in a callback style would look like:

```js
$('button').on('click', function() {
  // This click function finishes fast!
  // All it does is remember what it should go back to doing when the value has arrived.
  downloadContent(function(result) {
    slowTransformResult(result, function(transformedResult) {
      fastUpdateUI(transformedResult);
    });
  });
});
```

This works great for simple systems, but notice how it starts to get very nested very quickly.
It also requires you to change the interface of your functions to take a callback argument, which is totally different than the interface for normal return values.
This makes things get confusing quickly and people call this **callback hell**.

**Avoid using callbacks.**
Although lots of existing code works with them.
Try to use APIs that return promises or turn your callbacks into promises.

## Callbacks into Promises

Many functions you encounter will only accept callbacks.

```js
/**
 * Look up a temperature at a latitude and longitude.
 *
 * On success, call the function successCallback with the found temperature as a single argument.
 * On failure, call the function failureCallback with the error as a single argument.
 */
function lookupTemp(lat, lng, successCallback, failureCallback) {
  ...
}

/**
 * Update the HTML UI with the found temperature.
 */
function updateTempElement(temp) {
  ...
}

/**
 * Update the HTML UI with the encountered error.
 */
function updateErrorMessage(error) {
  ...
}

// Then you would kick off the temperature lookup using.
lookupTemp(lat, lng, updateTempElement, updateErrorMessage);
```

They're harder to work with, so if you want to convert them into promises, you can by wrapping them in a promise object manually.

The `Promise` constructor takes a single argument which is a function that takes two arguments: `resolve` and `reject`, they will be functions that should be called when the code has found a return value or encountered an error.

```js
/**
 * Wraps looking up a temperature in a promise.
 */
function lookupTempPromise(lat, lng) {
  return new Promise(function(resolve, reject) {
    // Call resolve(answer) when a return value is found.
    // Call reject(error) when an error is encountered.
    // lookupTemp will do that, so we can pass them in directly.
    lookupTemp(lat, lng, resolve, reject);
  });
}

lookupTemp(lat, lng).
  then(updateTempElement).
  catch(updateErrorMessage);
```
