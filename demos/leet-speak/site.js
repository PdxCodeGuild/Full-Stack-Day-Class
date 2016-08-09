'use strict';

/**
 * Convert a single letter from English to leet-speak.
 */
function convertLetterToLeetSpeak(originalLetter) {
  var originalCharToLeetChar = {
    o: '0',
    l: '1',
    e: '3',
    a: '4',
    t: '7'
  };
  var leetChar = originalCharToLeetChar[originalLetter];
  if (leetChar !== undefined) {
    return leetChar;
  } else {
    return originalLetter;
  }
}

/**
 * Convert a single word from English to leet-speak.
 *
 * E.g. 'cats' -> '(c4tZ)'
 */
function convertWordToLeetSpeak(originalWord) {
  var lowerOriginalWord = _.lowerCase(originalWord);
  // Map returns an array, so it needs to be re-joined into a string.
  var letterMappedLeetWord = _.join(
    _.map(lowerOriginalWord, convertLetterToLeetSpeak),
    '');
  var leetWord = letterMappedLeetWord;
  if (_.endsWith(letterMappedLeetWord, 's')) {
    // Same with slice, returns an array so re-join.
    var letterMappedLeetWordWithoutEndS = _.join(
      _.slice(letterMappedLeetWord, 0, -1),
      '');
    leetWord = letterMappedLeetWordWithoutEndS + 'Z';
  }
  return '(' + leetWord + ')';
}

/**
 * Convert an entire sentence from English to leet-speak, one word at a time.
 */
function convertSentenceToLeetSpeak(sentence) {
  var originalWords = _.words(sentence);
  var leetWords = _.map(originalWords, convertWordToLeetSpeak);
  return _.join(leetWords, ' ');
}

console.log(convertWordToLeetSpeak('rabbit'));
console.log(convertWordToLeetSpeak('pears'));
console.log(convertSentenceToLeetSpeak('rats at a bar grab at a star'));
