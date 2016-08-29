# Practice: Image Filter

Save your solution in a Django app, directory in `practice/`, in a branch, and in a Pull Request all named `imagefilter`.
This means there will be a directory `~/codeguild/practice/imagefilter/imagefilter`.

Make a web interface for applying some visual filters to an uploaded image.

Have a single index page.
It has a file upload form and a series of buttons underneath it, one for each available filter.
When a filter button is pressed, the filtered image is inserted into the current page as a preview.

You'll need an "AJAX" filter image endpoint.
It's only sort of AJAX because it's responding with image data, not JSON or XML.
It needs to take in the raw image file and the filter name and respond with the filtered image data.

Use the [Pillow](http://pillow.readthedocs.io/en/3.3.x/index.html) library to filter the images.
Provide the following filters:

* `grey` which returns a greyscale version of the image
* `blur` which Gaussian blurs the image by a little bit
* `invert` which inverts the colors of the image
