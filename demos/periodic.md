# Demo: Periodic Table

Using this [JSON periodic table dataset](https://raw.githubusercontent.com/andrejewski/periodic-table/master/data.json), make a periodic table explorer website.

Have a static style sheet that styles the whole site.

*   `GET /` will show a listing of all of the elements with a link to the below element page.

*   `GET /element/SYMBOL` will show a description of the element.
    Render HTML with the following info:

    * Name
    * Number
    * Mass
    * A swatch of the [CPK color](https://en.wikipedia.org/wiki/CPK_coloring)
    * Atomic Radius; if moused-over make the Ionic Radius

[Source](/demos/periodic)
