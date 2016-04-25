var convertWordToLeetSpeak = function(originalWord) {
    var originalCharToLeetChar = {
        "o": "0",
        "l": "1",
        "e": "3",
        "a": "4",
        "t": "7"
    };

    var workingLeetWord = originalWord.toLowerCase();
    for (var originalChar in originalCharToLeetChar) {
        var leetChar = originalCharToLeetChar[originalChar];
        while (workingLeetWord.includes(originalChar)) {
            workingLeetWord = workingLeetWord.replace(originalChar, leetChar);
        }
    }

    if (workingLeetWord.slice(-1) === "s") {
        workingLeetWord = workingLeetWord.slice(0, -1) + "Z";
    }

    return "(" + workingLeetWord + ")";
};

var convertSentenceToLeetSpeak = function(sentence) {
    var originalWords = sentence.split(" ");
    var leetWords = originalWords.map(convertWordToLeetSpeak);
    return leetWords.join(" ");
}

console.log(convertWordToLeetSpeak("rabbit"));
console.log(convertWordToLeetSpeak("pears"));
console.log(convertSentenceToLeetSpeak("rats at a bar grab at a star"));
