"""Tests for list comprehension exercises"""
from copy import deepcopy
import unittest

from lists import (get_vowel_names, power_list, flatten, reverse_difference,
                   matrix_add, transpose, get_factors, triples)


class GetVowelNamesTests(unittest.TestCase):

    """Tests for get_vowel_names."""

    def test_one_vowel_name(self):
        names = ["Alice", "Bob", "Christy", "Jules"]
        self.assertEqual(get_vowel_names(names), ["Alice"])

    def test_multiple_vowel_names(self):
        names = ["Scott", "arthur", "Jan", "Elizabeth"]
        self.assertEqual(get_vowel_names(names), ["arthur", "Elizabeth"])

    def test_empty(self):
        self.assertEqual(get_vowel_names([]), [])


class PowerListTests(unittest.TestCase):

    """Tests for power_list."""

    def test_integers(self):
        self.assertEqual(power_list([3, 2, 5]), [1, 2, 25])

    def test_floats(self):
        inputs = [78, 700, 82, 16, 2, 3, 9.5]
        outputs = [1, 700, 6724, 4096, 16, 243, 735091.890625]
        self.assertEqual(power_list(inputs), outputs)


class FlattenTests(unittest.TestCase):

    """Tests for flatten."""

    def test_3_by_4_matrix(self):
        matrix = [[row * 3 + incr for incr in range(1, 4)] for row in range(4)]
        flattened = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertEqual(flatten(matrix), flattened)


class ReverseDifferenceTests(unittest.TestCase):

    """Tests for reverse_difference."""

    def test_empty(self):
        self.assertEqual(reverse_difference([]), [])

    def test_one(self):
        self.assertEqual(reverse_difference([1]), [0])

    def test_two(self):
        self.assertEqual(reverse_difference([0, 0]), [0, 0])

    def test_three(self):
        self.assertEqual(reverse_difference([3, 2, 1]), [2, 0, -2])

    def test_four(self):
        self.assertEqual(reverse_difference([9, 8, 7, 6]), [3, 1, -1, -3])

    def test_five(self):
        inputs = [1, 2, 3, 4, 5]
        outputs = [-4, -2, 0, 2, 4]
        self.assertEqual(reverse_difference(inputs), outputs)


class MatrixAddTests(unittest.TestCase):

    """Tests for matrix_add."""

    def test_single_items(self):
        self.assertEqual(matrix_add([[5]], [[-2]]), [[3]])

    def test_two_by_two_matrixes(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4]]
        m3 = [[7, 8], [6, 5]]
        self.assertEqual(matrix_add(m1, m2), m3)

    def test_two_by_three_matrixes(self):
        m1 = [[1, 2, 3], [4, 5, 6]]
        m2 = [[-1, -2, -3], [-4, -5, -6]]
        m3 = [[0, 0, 0], [0, 0, 0]]
        self.assertEqual(matrix_add(m1, m2), m3)

    def test_input_unchanged(self):
        m1 = [[6, 6], [3, 1]]
        m2 = [[1, 2], [3, 4]]
        m1_original = deepcopy(m1)
        m2_original = deepcopy(m2)
        matrix_add(m1, m2)
        self.assertEqual(m1, m1_original)
        self.assertEqual(m2, m2_original)


class TransposeTests(unittest.TestCase):

    """Tests for transpose."""

    def test_empty(self):
        self.assertEqual(transpose([]), [])

    def test_single_item(self):
        self.assertEqual(transpose([[1]]), [[1]])

    def test_two_rows(self):
        self.assertEqual(transpose([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_three_rows(self):
        inputs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        outputs = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        self.assertEqual(transpose(inputs), outputs)


class GetFactorsTests(unittest.TestCase):

    """Tests for get_factors."""

    def test_2(self):
        self.assertEqual(get_factors(2), [1, 2])

    def test_6(self):
        self.assertEqual(get_factors(6), [1, 2, 3, 6])

    def test_100(self):
        self.assertEqual(get_factors(100), [1, 2, 4, 5, 10, 20, 25, 50, 100])


class TriplesTests(unittest.TestCase):

    """Tests for triples."""

    def test_triples_1(self):
        expected = []
        self.assertEqual(triples(1), expected)

    def test_triples_6(self):
        expected = [(3, 4, 5)]
        self.assertEqual(triples(6), expected)

    def test_triples_25(self):
        expected = [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17),
                    (9, 12, 15), (12, 16, 20)]
        self.assertEqual(triples(25), expected)


if __name__ == "__main__":
    unittest.main()
