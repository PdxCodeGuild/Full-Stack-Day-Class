'use strict';

/**
 * Create an empty completer.
 *
 * Given a prefix, it will return valid completions.
 */
function Completer() {
  // Store known completions as properties in an object.
  // This is because it is easy to delete an arbirary value.
  this.completions = {};
}
Completer.prototype = {
  /**
   * Add a new completion.
   *
   * Only known completions will be returned.
   */
  addCompletion: function(newCompletion) {
    // Just store a dummy value so the completion is a property.
    this.completions[newCompletion] = 1;
  },
  /**
   * Remove an existing completion.
   *
   * Will no longer be returned.
   */
  removeCompletion: function(existingCompletion) {
    delete this.completions[existingCompletion];
  },
  /**
   * Return all previously-added completions that match a given prefix.
   */
  complete: function(prefix) {
    return _.filter(_.keys(this.completions), function(completion) {
      return completion.startsWith(prefix);
    });
  }
};

var fruitCompleter = new Completer();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('banana');
console.log(fruitCompleter.complete('a'));
console.log(fruitCompleter.complete('b'));
fruitCompleter.removeCompletion('apple');
console.log(fruitCompleter.complete('a'));

/**
 * Create an empty weighted completer.
 *
 * Given a prefix, it will return valid completions in order by weight.
 */
function WeightedCompleter() {
  this.completionToWeight = {};
}
WeightedCompleter.prototype = {
  /**
   * Add a new completion with no weight.
   *
   * Only known completions will be returned.
   */
  addCompletion: function(newCompletion) {
    this.completionToWeight[newCompletion] = 0;
  },
  /**
   * Remove an existing completion.
   *
   * Will no longer be returned.
   */
  removeCompletion: function(existingCompletion) {
    delete this.completionToWeight[existingCompletion];
  },
  /**
   * Add weight to an existing completion.
   *
   * It will appear earlier in the results.
   */
  selectCompletion: function(completion) {
    this.completionToWeight[completion] += 1;
  },
  /**
   * Return all previously-added completions that match a given prefix in order by weight descending, then alphabetical order.
   */
  complete: function(prefix) {
    var matchingCompletions = _.filter(
      _.keys(this.completionToWeight),
      function(completion) {
        return completion.startsWith(prefix);
      });
    // Store the weights in a local variable so they are easily captured by the sort key functions.
    var completionToWeight = this.completionToWeight;
    return _.sortBy(
      matchingCompletions,
      // Can take a list of key functions.
      // Will sort on the return value of each one, in order.
      [
        // Sort by weight first.
        function(completion) {
          // Negative so descending.
          return -completionToWeight[completion];
        },
        // Then sort on string value or alphabetical order.
        _.identity
      ]);
  }
};

var fruitCompleter = new WeightedCompleter();
fruitCompleter.addCompletion('apple');
fruitCompleter.addCompletion('avocado');
fruitCompleter.addCompletion('anise');
fruitCompleter.addCompletion('banana');
console.log(fruitCompleter.complete('a'));
fruitCompleter.selectCompletion('avocado');
console.log(fruitCompleter.complete('a'));
fruitCompleter.selectCompletion('apple');
fruitCompleter.selectCompletion('apple');
console.log(fruitCompleter.complete('a'));
