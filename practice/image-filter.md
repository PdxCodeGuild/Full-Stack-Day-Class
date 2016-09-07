# Practice: Image Filter

Save your solution in a Django app, directory in `practice/` and in a branch named `image_filter`.
This means there will be a directory `~/codeguild/practice/image_filter/image_filter`.

Make a web interface for applying some visual filters to an uploaded image.

Have a single index page.
It has a file upload form and a series of buttons underneath it, one for each available filter.
When a filter button is pressed, the filtered image is inserted into the current page as a preview.

You'll need an "AJAX" filter image endpoint `POST /filter`.
It needs to take in the raw image file and the filter name in a POST body, and respond with the filtered image data in JPEG format.
Look up how to to make a view respond with an appropriate content type so the browser knows your data is an image.

Use the [Pillow](http://pillow.readthedocs.io/en/3.3.x/index.html) library to filter the images.
Provide the following filters:

* `grey` which returns a greyscale version of the image
* `blur` which Gaussian blurs the image by a little bit
* `invert` which inverts the colors of the image

There will be a lot of hoops to jump through in JS to get this to work.
You'll have to use:

* [FormData](https://developer.mozilla.org/en-US/docs/Web/API/FormData?redirectlocale=en-US&redirectslug=Web%2FAPI%2FXMLHttpRequest%2FFormData) to assemble the data for AJAX sending.
* [Some way of feeding that to jQuery's AJAX](http://stackoverflow.com/questions/5392344/sending-multipart-formdata-with-jquery-ajax).
* [Inline Base 64 image encoding](http://www.bigfastblog.com/embed-base64-encoded-images-inline-in-html) because there is no way to have the `img` tag's `src` attribute make a POST request for the image.
* [Some way of converting a JS string of bytes to base 64](https://developer.mozilla.org/en-US/docs/Web/API/WindowBase64/Base64_encoding_and_decoding#Solution_.232_.E2.80.93_rewriting_atob()_and_btoa()_using_TypedArrays_and_UTF-8).
