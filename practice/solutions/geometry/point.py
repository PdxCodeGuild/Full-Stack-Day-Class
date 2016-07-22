class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    def __repr__(self):
        return 'Point({!r}, {!r})'.format(self.x, self.y)


def distance_to(self, other_point):
    return (
               (self.x - other_point.x) ** 2 +
               (self.y - other_point.y) ** 2
           ) ** 0.5


def move_by(self, dx, dy):
    self.x += dx
    self.y += dy
