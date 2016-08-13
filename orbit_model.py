#!/usr/bin/env python3

import unittest
import random
import time
import math
import argparse

class Orbit(object):
    def __init__(self, fuzzy=0):
        self.start=time.time()

    @property
    def radius(self):
        return 10

    @property
    def theta(self):
        return (self.start - time.now()) % (2 * math.pi)


class TestOrbit(unittest.TestCase):
    def setup(self):
        self.orbit = Orbit()

    def test_orbit(self):
        self.assertEqual(self.orbit.radius, 10)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run an orbit')
    mode_parser = parser.add_subparsers(title='unittests', dest='mode')
    unittest_parser = mode_parser.add_parser('unittest',
        parents=[parser], add_help=False,
        help='Run the unittests')
    run_parser = mode_parser.add_parser('run',
        parents=[parser], add_help=False,
        help='Run the simulation')
    args = parser.parse_args()
    print(args)
    unittest.main()
