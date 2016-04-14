import unittest
import geometry


class PointTest(unittest.TestCase):
    def test_point_init(self):
        p = geometry.Point(1, 2)
        assert p.x == 1
        assert p.y == 2

    def test_distance_to(self):
        p1 = geometry.Point(0, 0)
        p2 = geometry.Point(2, 0)
        found = p1.distance_to(p2)
        assert found == 2

    def test_move_by(self):
        p = geometry.Point(1, 2)
        p.move_by(1, 1)
        assert p.x == 2
        assert p.y == 3

    def test_move_subtract(self):
        p = geometry.Point(1, 2)
        p.move_subtract(1, 1)
        assert p.x == 0
        assert p.y == 1

    def test_eq_not(self):
        p1 = geometry.Point(0, 0)
        p2 = geometry.Point(2, 0)
        assert p1 != p2

    def test_eq(self):
        p1 = geometry.Point(0, 0)
        p2 = geometry.Point(0, 0)
        assert p1 == p2

    def test_repr(self):
        p = geometry.Point(1, 2)
        found = repr(p)
        expected = 'Point(1, 2)'
        assert found == expected
