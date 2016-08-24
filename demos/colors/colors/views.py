"""colors Views."""
from django.http import HttpResponse

from .logic import find_things_of_color


def render_colored_things(request, color):
    """Find all things of a given color and write out the list of them.

    If no things of a color are found, return a 404.
    """
    found_things = find_things_of_color(color)
    if len(found_things) > 0:
        return HttpResponse(', '.join(found_things))
    else:
        return HttpResponse('not found', status=404)
