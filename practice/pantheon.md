# Practice: Pantheon

Save your solution in a Django app, directory in `practice/`, and in a branch all named `pantheon`.
This means there will be a directory `~/codeguild/practice/pantheon/pantheon`.

Make a website for exploring the [Pantheon](http://pantheon.media.mit.edu/) data set of "culturally popular people" (but who's really to say that?).

First [download the data set](http://pantheon.media.mit.edu/pantheon.tsv).
It is a UTF-8 TSV file.
Each row / entry is a person and some simple facts about them.

We're going to make a web interface for the dataset.
Include a static style sheet that styles all of the pages.

*   `GET /` will list of all countries in alphabetical order and link each one to the below country listing page.

*   `GET /country/COUNTRY_CODE` will list all industries known for a country in alphabetical order and link each one to the below industry listing page.

*   `GET /country/COUNTRY_CODE/industry/INDUSTRY` will list all persons in that industry in alphabetical order and link each one to the below person description page.

*   `GET /persons/CUR_ID` will show a description page for a specific person.
    Render a HTML page in a pretty way that displays:

    * Name
    * Birth Year
    * Country
    * Occupation
    * Google Map of Location (include static JS to perform this)
    * (Trite, but) have the page style be templated to be pink or blue on the gender of the person

Practice MVC separation: the model should just contain data loading and retrieval functions, views should just contain HTTP request decoding and response encoding functions, and the controller / logic should contain all of the "business logic".
This program will have pretty minimal logic, because it is basically just a display app.

You can load the TSV dataset using the [csv](https://docs.python.org/3/library/csv.html) module in the standard library.
Configure its [reader](https://docs.python.org/3/library/csv.html#csv.reader) to use a tab literal `'\t'` as the **delimiter**.

Have this data be loaded into global variables in the model module on _import_.
Then each HTTP request can quickly retrieve the data it needs.
On import, prepare data structures that will allow each view to access the data it needs easily.
