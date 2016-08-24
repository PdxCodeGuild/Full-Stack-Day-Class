# Practice: Bus Stop Finder

Save your solution in a directory in `practice/` and in a branch named `bus-stop`.
Your HTML file should be named `index.html`, your CSS file named `site.css`, and your JS file named `site.js` in that directory.
Any keys should live in a `secrets.js`.

Using the [Web Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation) and the [TriMet Web Services API](http://developer.trimet.org/ws_docs/), write a web page that, when loaded, gives you a list of all of the bus lines that have stops within 100 meters of your current location.
Then provide a link for each bus line to it's map (e.g. [line 14 map](http://trimet.org/schedules/r014.htm)).

## Secure Origin

Chrome [disallows the geolocation call from successfully returning](https://developers.google.com/web/updates/2016/04/geolocation-on-secure-contexts-only) if the current page is not served via HTTPS or is from `localhost`; the `file://` scheme is not deemed secure.

Thus, you have to formally serve your page content.
Conveniently, Python has a [built-in HTTP server](https://docs.python.org/3/library/http.server.html) that can serve the working directory over HTTP with the following command.

```bash
~/codeguild/bus-stop $ python -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 ...
```

You can now go to <http://localhost:8000/index.html> to view `index.html` and geolocation calls will succeed.

## Advanced

Add a Google Map that visually displays markers for each stop nearby.
