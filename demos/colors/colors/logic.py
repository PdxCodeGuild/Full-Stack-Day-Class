"""colors Logic."""
from .models import THINGS_AND_COLORS


def find_things_of_color(find_color):
    """Return all things in the database of a given color.

    >>> sorted(find_things_of_color('blue'))
    ['blueberry', 'chair', 'sky']
    >>> find_things_of_color('white')
    []
    """
    return [
        thing
        for thing, color
        in THINGS_AND_COLORS
        if color == find_color
    ]
