"""colors Views."""
from django.http import HttpResponse

from .logic import find_things_of_color


def get_color(request, color):
    found_things = find_things_of_color(color)
    if len(found_things) > 0:
        return HttpResponse(', '.join(found_things))
    else:
        return HttpResponse('not found', status=404)
