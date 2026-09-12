#!/usr/bin/env python3

import unittest

from src.negative_to_positive import negative_to_positive


class TestNegativeToPositive(unittest.TestCase):

    def test_n_equals_2(self):
        result = negative_to_positive(2)
        self.assertEqual(
            result, [-2, -1, 1, 2],
            msg="negative_to_positive(2) should be [-2, -1, 1, 2]: count "
                "down from -2 to -1, skip 0, then count up from 1 to 2. "
                "Got %r." % (result,))

    def test_n_equals_3(self):
        result = negative_to_positive(3)
        self.assertEqual(
            result, [-3, -2, -1, 1, 2, 3],
            msg="negative_to_positive(3) should be [-3, -2, -1, 1, 2, 3]. "
                "Got %r." % (result,))

    def test_n_equals_7(self):
        result = negative_to_positive(7)
        self.assertEqual(
            result, [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7],
            msg="negative_to_positive(7) should list every integer from -7 "
                "to 7, skipping 0. Got %r." % (result,))

    def test_n_equals_5(self):
        result = negative_to_positive(5)
        self.assertEqual(
            result, [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5],
            msg="negative_to_positive(5) should list every integer from -5 "
                "to 5, skipping 0. Got %r." % (result,))

    def test_n_equals_1(self):
        result = negative_to_positive(1)
        self.assertEqual(
            result, [-1, 1],
            msg="negative_to_positive(1) should be [-1, 1]: 0 must be "
                "skipped even though it lies between -1 and 1. "
                "Got %r." % (result,))

    def test_zero_never_appears(self):
        result = negative_to_positive(4)
        self.assertNotIn(
            0, result,
            msg="negative_to_positive(4) must not include 0. Got %r."
                % (result,))

    def test_return_type(self):
        result = negative_to_positive(2)
        self.assertIsInstance(
            result, list,
            msg="negative_to_positive should return a list. Got %s."
                % (type(result),))


if __name__ == '__main__':
    unittest.main()
