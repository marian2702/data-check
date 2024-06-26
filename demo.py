"""Dummy challenge for Kitt Demo"""
import unittest

def circle_area(radius):
    return 3.14 * radius * radius

class TestDemo(unittest.TestCase):
    def test_returns_3_14_for_radius_1(self):
        expected = 3.14
        actual = circle_area(1)
        self.assertAlmostEqual(expected, actual, 2)

    def test_returns_78_5_for_radius_5(self):
        expected = 78.5
        actual = circle_area(5)
        self.assertAlmostEqual(expected, actual, 1)

    def test_returns_zero_for_negative_radius(self):
        expected = 0
        actual = circle_area(-1)
        self.assertEqual(expected, actual)
