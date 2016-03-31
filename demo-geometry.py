class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return (
            (self.x - other_point.x) ** 2
            + (self.y - other_point.y) ** 2
        ) ** 0.5

    def move_to(self, dx, dy):
        return Point(self.x + dx, self.y + dy)

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y

    def __str__(self):
        return 'Point({}, {})'.format(self.x, self.y)

class Rectangle:
    def __init__(self, bottom_left_corner, w, h):
        self.bottom_left_corner = bottom_left_corner
        self.w = w
        self.h = h

    def contains(self, point):
        x_is_inside = (
            point.x >= self.bottom_left_corner.x
            and point.x <= (self.bottom_left_corner.x + self.w)
        )
        y_is_inside = (
            point.y >= self.bottom_left_corner.y
            and point.y <= (self.bottom_left_corner.y + self.h)
        )
        return x_is_inside and y_is_inside

    def find_center(self):
        return Point(
            self.bottom_left_corner.x + self.w / 2,
            self.bottom_left_corner.y + self.h / 2,
        )

    def __eq__(self, other_rect):
        return (
            self.bottom_left_corner == other_rect.bottom_left_corner
            and self.w == other_rect.w and self.h == other_rect.h
        )

    def __str__(self):
        return 'Rectangle({}, {}, {})'.format(
            self.bottom_left_corner,
            self.w,
            self.h
        )

house = Point(10, 9)
work = Point(5, 2)
print('House to work distance:', house.distance_to(work))

city = Rectangle(Point(5, 5), 10, 10)
print('House in city:', city.contains(house))
print('Work in city:', city.contains(work))

city_center = city.find_center()
print('City center:', city_center)

cats_house = Point(10, 9)
identical_city = Rectangle(Point(5, 5), 10, 10)
different_city = Rectangle(Point(13, 13), 10, 10)
print('My cat\'s house and mine are equal:', house == cats_house)
print('Two identical cities are equal:', city == identical_city)
print('Two different cities are equal:', city == different_city)

moved_house = house.move(1, -1)
print('After moving my house:', moved_house)
