#!/usr/bin/env python3

import unittest
from orbit_model import Orbit
import time

class TestOrbit(unittest.TestCase):
    def setUp(self):
        self.orbit = Orbit()

    def test_radius(self):
        self.assertEqual(self.orbit.radius, 10)

    def test_theta(self):
        first = self.orbit.theta
        time.sleep(1/100)
        second = self.orbit.theta
        self.assertNotEqual(first, second)

if __name__ == '__main__':
    unittest.main()
