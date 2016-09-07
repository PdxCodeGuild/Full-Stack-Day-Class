"""image_filter Views."""
from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image

from . import logic


def render_index(request):
    """View function that renders the interface form."""
    return render(request, 'image_filter/index.html')


def _read_image_request(request, image_field_name):
    """Convert an image posted in the request to a PIL image.

    Remember, that the POST request needs to be submitted as "multipart/form-data" for the file data to appear.
    """
    in_image_file = request.FILES[image_field_name]
    return Image.open(in_image_file)


def _write_image_response(image):
    """Convert a PIL image to a JPEG Django HTTP response."""
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, 'JPEG')
    return response


def return_filtered_image(request):
    """AJAX / API endpoint that accepts an image and filter out of a POST request, filters it, and returns a JPEG
    response.

    Remember, that the POST request needs to be submitted as "multipart/form-data" for the file data to appear.
    """
    in_image = _read_image_request(request, 'image')
    filter_name = request.POST['filter']

    if filter_name == 'gray':
        out_image = logic.filter_gray(in_image)
    elif filter_name == 'blur':
        out_image = logic.filter_blur(in_image)
    elif filter_name == 'invert':
        out_image = logic.filter_invert(in_image)
    else:
        return HttpResponse('unknown filter: {!r}'.format(filter_name), code=400)

    return _write_image_response(out_image)
