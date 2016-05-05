'use strict';

/**
 * Convert a single word from English to leet-speak.
 *
 * E.g. 'cats' -> '(c4tZ)'
 */
function convertWordToLeetSpeak(originalWord) {
  var originalCharToLeetChar = {
    o: '0',
    l: '1',
    e: '3',
    a: '4',
    t: '7'
  };
  var workingLeetWord = _.lowerCase(originalWord);

  workingLeetWord = _.reduce(
    _.keys(originalCharToLeetChar),
    function(workingLeetWord, originalChar) {
      if (_.includes(workingLeetWord, originalChar)) {
        var leetChar = originalCharToLeetChar[originalChar];
        return _.replace(workingLeetWord, originalChar, leetChar);
      } else {
        return workingLeetWord;
      }
    },
    workingLeetWord);

  if (_.endsWith(workingLeetWord, 's')) {
    workingLeetWord = _.join(_.slice(workingLeetWord, 0, -1), '') + 'Z';
  }

  return '(' + workingLeetWord + ')';
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
