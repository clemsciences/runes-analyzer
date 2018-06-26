

import unittest
import data

__author__ = ["Clément Besnier <clemsciences@aol.com>"]


class Tests(unittest.TestCase):
    def test_elder_futhark(self):
        self.assertListEqual([], data.OLD_FUTHARK)
