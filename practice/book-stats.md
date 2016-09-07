# Practice: Book Stats

Save your solution in a Django app, directory in `practice/`, and in a branch all named `bookstats`.
This means there will be a directory `~/codeguild/practice/bookstats/bookstats`.

Find a book on [Project Gutenberg](http://www.gutenberg.org).
Download it as a UTF-8 text file.
Do some pre-processing in your `models` module, then expose a public interface via `logic` that:

* `get_word_count(word)` returns the number of times a word is used in the book
* `get_word_frequency(word)` returns the frequency of a word in the book (times used / total words)

Make this pre-processing very stupid: just split by spaces.
Doing interesting text normalization for statistics can get exceedingly complicated (c.f. [tokenization](http://nlp.stanford.edu/IR-book/html/htmledition/tokenization-1.html), [stop words](http://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html), [normalization](http://nlp.stanford.edu/IR-book/html/htmledition/normalization-equivalence-classing-of-terms-1.html), [lemmatization](http://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html)) but don't worry about that here.

Now make a web interface to this data:

*   `GET /` an index page with a search form that allows a user to put in a single word

*   `GET /stats?word=WORD` responds with a JSON object with stats about that word

    ```json
    {
      "word": "bats",
      "word_count": 123,
      "word_freq": 0.0005,
    }
    ```

When the search on the index page is preformed, use AJAX to update the page with the found stats.

## Advanced

Allow the user to compare the stats of multiple words.
Whenever the user re-searches, it appends some new stats to the page.
Add a button to remove the stats of some word.
