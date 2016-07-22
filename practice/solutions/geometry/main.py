from rectangle import Rectangle
from point import Point


def main():
    house = Point(10, 9)
    print('House is at X:', house.x)
    print('House is at Y:', house.y)
    work = Point(5, 2)
    print('House to work distance:', house.distance_to(work))

    city = Rectangle(Point(5, 5), 10, 10)
    print('City corner is:', city.bottom_left_corner)
    print('City width:', city.w)
    print('City height:', city.h)
    print('House in city:', city.contains(house))
    print('Work in city:', city.contains(work))

    city_center = city.find_center()
    print('City center:', city_center)

    cats_house = Point(10, 9)
    identical_city = Rectangle(Point(5, 5), 10, 10)
    different_city = Rectangle(Point(13, 13), 10, 10)
    print("My cat's house and mine are equal:", house == cats_house)
    print('Two identical cities are equal:', city == identical_city)
    print('Two different cities are equal:', city == different_city)

    house.move_by(1, -1)
    print('After moving my house:', house)


if __name__ == '__main__':
    main()
