# Client-Side Templated Web Applications

The basic rendering process for our web apps has been a single pipeline.

1. Logic sends models to...
1. Views which prepare fully-formed HTML for...
1. Browser

Then we added in some AJAX for more dynamism.

1. Logic sends models to...
1. Views which prepare fully-formed HTML / JSON for...
1. Browser

There was nothing that we could do with AJAX that we couldn't do with standard templating.
So why do it?

* No page refreshing; more flexible request situations
* Possibly smaller data transfer; only data, not full display

What if we keep moving in this direction?

1. Logic sends models to...
1. Views which prepare JSON for...
1. Browser

In a sense, you only write a data-driven API that exposes your business functionality, then separately write a UI that has to rigorously use that API via JS.

This is cool because it has some additional advantages.

* Even smaller data transfer; JS once, small data from there on out
* Totally separate presentation and logic by HTTP interface; makes teams
* Identical server could power a mobile app or be exposed as a public API

* [Handlebars](http://handlebarsjs.com)
* [Backbone](http://backbonejs.org)
* [Angular](https://angular.io)
* [React](https://facebook.github.io/react/)
