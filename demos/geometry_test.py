import unittest
import geometry

class PointTest(unittest.TestCase):
    def test_point(self):
        p = geometry.Point(1, 2)
        self.assertEquals(p.x, 1)
        self.assertEquals(p.y, 2)
