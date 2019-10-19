"""

"""

import unittest
from runesanalyzer import data

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


class Tests(unittest.TestCase):
    def test_elder_futhark(self):
        self.assertListEqual(['ᚠ', 'ᚢ', 'ᚦ', 'ᚨ', 'ᚱ', 'ᚲ', 'ᚷ', 'ᚹ', 'ᚺ', 'ᚾ', 'ᛁ', 'ᛃ', 'ᛇ,' 'ᛈ', 'ᛉ', 'ᛊ', 'ᛏ', 'ᛒ',
                              'ᛖ', 'ᛗ', 'ᛚ', 'ᛜ', 'ᛟ', 'ᛞ'], data.ELDER_FUTHARK)
