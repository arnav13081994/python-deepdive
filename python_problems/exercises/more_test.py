"""Tests for dictionary exercises"""
import unittest

from more import (flip_dict, get_ascii_codes, dict_from_truple,
                  dict_from_tuple, get_all_factors)


class GetASCIICodeTests(unittest.TestCase):

    """Tests for get_ascii_codes."""

    def test_multiple_words(self):
        words = ["hello", "bye", "yes", "no", "python"]
        outputs = {
            'yes': [121, 101, 115],
            'hello': [104, 101, 108, 108, 111],
            'python': [112, 121, 116, 104, 111, 110],
            'no': [110, 111],
            'bye': [98, 121, 101],
        }
        self.assertEqual(get_ascii_codes(words), outputs)


class GetAllFactorsTests(unittest.TestCase):

    """Tests for get_all_factors."""

    def test_small_numbers(self):
        inputs = {1, 2, 3, 4}
        outputs = {1: [1], 2: [1, 2], 3: [1, 3], 4: [1, 2, 4]}
        self.assertEqual(get_all_factors(inputs), outputs)

    def test_larger_numbers(self):
        inputs = {62, 293, 314}
        outputs = {62: [1, 2, 31, 62], 293: [1, 293], 314: [1, 2, 157, 314]}
        self.assertEqual(get_all_factors(inputs), outputs)


class FlipDictTests(unittest.TestCase):

    """Tests for flip_dict."""

    def test_no_collisions(self):
        inputs = {
            'Python': "2015-09-15",
            'Java': "2015-09-14",
            'C': "2015-09-13",
        }
        outputs = {
            '2015-09-13': 'C',
            '2015-09-15': 'Python',
            '2015-09-14': 'Java',
        }
        self.assertEqual(flip_dict(inputs), outputs)


class DictFromTrupleTests(unittest.TestCase):

    """Tests for dict_from_truple."""

    def test_three_tuples(self):
        inputs = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        outputs = {1: (2, 3), 4: (5, 6), 7: (8, 9)}
        self.assertEqual(dict_from_truple(inputs), outputs)


class DictFromTupleTests(unittest.TestCase):

    """Tests for dict_from_tuple."""

    def test_four_items(self):
        inputs = [(1, 2, 3, 4), (5, 6, 7, 8)]
        outputs = {1: (2, 3, 4), 5: (6, 7, 8)}
        self.assertEqual(dict_from_tuple(inputs), outputs)

    def test_three_items(self):
        inputs = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
        outputs = {1: (2, 3), 4: (5, 6), 7: (8, 9)}
        self.assertEqual(dict_from_tuple(inputs), outputs)


if __name__ == "__main__":
    unittest.main()
