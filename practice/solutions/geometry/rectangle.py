from point import Point


class Rectangle:
    def __init__(self, bottom_left_corner, w, h):
        self.bottom_left_corner = bottom_left_corner
        self.w = w
        self.h = h

    def __eq__(self, other_rect):
        return (
            self.bottom_left_corner == other_rect.bottom_left_corner and
            self.w == other_rect.w and self.h == other_rect.h
        )

    def __repr__(self):
        return 'Rectangle({!r}, {!r}, {!r})'.format(
            self.bottom_left_corner,
            self.w,
            self.h
        )


def contains(self, point):
    x_is_inside = (
        self.bottom_left_corner.x <= point.x <= (self.bottom_left_corner.x + self.w)
    )
    y_is_inside = (
        self.bottom_left_corner.y <= point.y <= (self.bottom_left_corner.y + self.h)
    )
    return x_is_inside and y_is_inside


def find_center(self):
    return Point(
        self.bottom_left_corner.x + self.w / 2,
        self.bottom_left_corner.y + self.h / 2,
    )
