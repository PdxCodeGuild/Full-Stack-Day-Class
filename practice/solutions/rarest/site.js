'use strict';

/**
 * Return the property value that occurs least frequently in the given object.
 */
function findRarestValue(obj) {
  var values = _.values(obj);
  var valueToCount = _.countBy(values);
  return _.minBy(values, function(value) {
    return valueToCount[value];
  });
}

/**
 * Return the list of keys that all share the least frequently occuring value.
 */
function findRarestKeys(obj) {
  var valueToKeys = _.groupBy(_.keys(obj), function(key) {
    return obj[key];
  });
  return _.minBy(_.values(valueToKeys), function(keys) {
    return keys.length;
  });
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
console.log(findRarestKeys(namesToAges));
