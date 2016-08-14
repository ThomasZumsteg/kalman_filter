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
        return (self.start - time.time()) % (2 * math.pi)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run an orbit')
    subparser = parser.add_subparsers(help='Program mode', dest='mode')
    daemon_parser = subparser.add_parser('daemon',
        parent=[parser],
        help='Run in daemon mode')
    run_parser = subparser.add_parser('run',
        help='Run in foreground')
    args = parser.parse_args()
    if args.mode == 'daemon':
        print('Not implemented yet')
    elif args.mode == 'run':
        print('Not implemented yet')
    else:
        parser.print_help()
