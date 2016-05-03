var convertWordToLeetSpeak = function(originalWord) {
    var originalCharToLeetChar = {
        "o": "0",
        "l": "1",
        "e": "3",
        "a": "4",
        "t": "7"
    };

    var workingLeetWord = _.lowerCase(originalWord);
    for (var originalChar in originalCharToLeetChar) {
        var leetChar = originalCharToLeetChar[originalChar];
        while (_.includes(workingLeetWord, originalChar)) {
            workingLeetWord = _.replace(workingLeetWord, originalChar, leetChar);
        }
    }

    if (_.endsWith(workingLeetWord, "s")) {
        workingLeetWord = _.join(_.slice(workingLeetWord, 0, -1), "") + "Z";
    }

    return "(" + workingLeetWord + ")";
};

var convertSentenceToLeetSpeak = function(sentence) {
    var originalWords = _.words(sentence);
    var leetWords = _.map(originalWords, convertWordToLeetSpeak);
    return _.join(leetWords, " ");
}

console.log(convertWordToLeetSpeak("rabbit"));
console.log(convertWordToLeetSpeak("pears"));
console.log(convertSentenceToLeetSpeak("rats at a bar grab at a star"));
