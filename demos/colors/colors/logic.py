"""colors Logic."""

def find_things_of_color(find_color):
    """

    >>>
    """
    return [
        thing
        for thing, color
        in THINGS_AND_COLORS
        if color == find_color
    ]

