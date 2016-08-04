'use strict';

/**
 * Return the object value that occurs least frequently.
 */
function findRarestValue(obj) {
  var origKeys = _.keys(obj);
  var origValueToOrigKeys = _.groupBy(origKeys, function(origKey) {
    return obj[origKey];
  });
  var origValueToCount = _.mapValues(origValueToOrigKeys, function(origKeys) {
    return origKeys.length;
  });
  var origValues = _.values(obj);
  var minCountKey = _.minBy(origValues, function(origValue) {
    return origValueToCount[origValue];
  });
  return minCountKey;
}

var namesToAges = {
  'Alyssa': 22,
  'Charley': 25,
  'Dan': 25,
  'Jeff': 20,
  'Kasey': 20,
  'Kim': 20,
  'Morgan': 25,
  'Ryan': 25,
  'Stef': 22
};

console.log(findRarestValue(namesToAges));
