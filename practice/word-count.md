# Practice: Word Count

Save your solution as `practice/word-count.py`.

Find a book on [Project Gutenberg](http://www.gutenberg.org).
Download it as a UTF-8 text file.

* Count how often each unique word is used, then print the most frequent top 10 out with their counts.
* Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.

Pairs of words overlap.

```
The cat in the hat. -> The cat, cat in, in the, the hat.
```

## Advanced

*   Allow the user to enter a word and get the most likely words to follow the given word.
Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word.

    ```
    Input? Mr.
    The most likely pair starting with "Mr." is "Mr. Darcy".
    ```

*   Normalize all of the words so differences in capitalization and punctuation attached to words don't affect the counts.

*   Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.

*   Chain together that ability to generate random sentences, one word at a time, from a given starting word.
This is a language model.
