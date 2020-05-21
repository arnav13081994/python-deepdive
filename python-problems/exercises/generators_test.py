"""Test for generator exercises"""
import unittest

from generators import (is_prime, all_together, interleave, first_prime_over,
                        translate, is_anagram, parse_ranges)


class PrimalityTests(unittest.TestCase):

    """Tests for is_prime."""

    def test_21(self):
        self.assertFalse(is_prime(21))

    def test_23(self):
        self.assertTrue(is_prime(23))


class AllTogetherTests(unittest.TestCase):

    """Tests for all_together."""

    def test_list_and_tuple(self):
        outputs = list(all_together([1, 2], (3, 4)))
        expected = [1, 2, 3, 4]
        self.assertEqual(outputs, expected)

    def test_with_strings(self):
        outputs = list(all_together([1, 2], (3, 4), "hello"))
        expected = [1, 2, 3, 4, 'h', 'e', 'l', 'l', 'o']
        self.assertEqual(outputs, expected)

    def test_empty_list(self):
        outputs = list(all_together([], (), '', [1, 2]))
        self.assertEqual(outputs, [1, 2])

    def test_iterator(self):
        outputs = all_together([1], [2])
        self.assertEqual(list(outputs), [1, 2])
        self.assertEqual(list(outputs), [])

    def test_is_iterator(self):
        numbers = all_together([1, 2], (3, 4))
        output = all_together(numbers, (5, 6))
        self.assertEqual(next(output), 1)
        self.assertEqual(next(numbers), 2)


class InterleaveTests(unittest.TestCase):

    """Tests for interleave."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_empty_lists(self):
        self.assertIterableEqual(interleave([], []), [])

    def test_single_item_each(self):
        self.assertIterableEqual(interleave([1], [2]), [1, 2])

    def test_two_items_each(self):
        self.assertIterableEqual(interleave([1, 2], [3, 4]), [1, 3, 2, 4])

    def test_four_items_each(self):
        in1 = [1, 2, 3, 4]
        in2 = [5, 6, 7, 8]
        out = [1, 5, 2, 6, 3, 7, 4, 8]
        self.assertIterableEqual(interleave(in1, in2), out)

    def test_none_value(self):
        in1 = [1, 2, 3, None]
        in2 = [4, 5, 6, 7]
        out = [1, 4, 2, 5, 3, 6, None, 7]
        self.assertIterableEqual(interleave(in1, in2), out)

    def test_non_sequences(self):
        in1 = [1, 2, 3, 4]
        in2 = (n**2 for n in in1)
        out = [1, 1, 2, 4, 3, 9, 4, 16]
        self.assertIterableEqual(interleave(in1, in2), out)

    def test_response_is_iterator(self):
        in1 = [1, 2, 3]
        in2 = [4, 5, 6]
        output = interleave(in1, in2)
        self.assertEqual(iter(output), iter(output))
        list(output)
        self.assertEqual(list(output), [])


class FirstPrimeOverTests(unittest.TestCase):

    """Tests for first_prime_over."""

    def test_first_prime_over_one_million(self):
        self.assertEqual(first_prime_over(1000000), 1000003)

    def test_first_prime_over_three_million(self):
        self.assertEqual(first_prime_over(3000000), 3000017)


class TranslateTests(unittest.TestCase):

    """Tests for translate."""

    def test_cat(self):
        self.assertEqual(translate("gato"), "cat")

    def test_the_cat(self):
        self.assertEqual(translate("el gato"), "the cat")

    def test_cat_in_house(self):
        inputs = "el gato esta en la casa"
        outputs = "the cat is in the house"
        self.assertEqual(translate(inputs), outputs)


class ParseRangesTests(unittest.TestCase):

    """Tests for parse_ranges."""

    def test_single_range(self):
        self.assertEqual(
            list(parse_ranges('1-4')),
            [1, 2, 3, 4],
        )

    def test_three_ranges(self):
        self.assertEqual(
            list(parse_ranges('1-2,4-4,8-10')),
            [1, 2, 4, 8, 9, 10],
        )

    def test_four_ranges(self):
        self.assertEqual(
            list(parse_ranges('0-0,4-8,20-21,43-45')),
            [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45],
        )

    def test_is_iterator(self):
        self.assertEqual(
            next(parse_ranges('1-4')),
            1,
        )


class IsAnagramTests(unittest.TestCase):

    """Tests for is_anagram."""

    def test_short_anagram(self):
        self.assertTrue(is_anagram("tea", "eat"))

    def test_different_lengths(self):
        self.assertFalse(is_anagram("tea", "treat"))

    def test_sink_and_skin(self):
        self.assertTrue(is_anagram("sink", "skin"))

    def test_same_letters_different_lengths(self):
        self.assertFalse(is_anagram("sinks", "skin"))

    def test_different_capitalization(self):
        self.assertTrue(is_anagram("Trey", "Yert"))
        self.assertTrue(is_anagram("Listen", "silent"))

    def test_spaces_ignored(self):
        phrase1 = "William Shakespeare"
        phrase2 = "I am a weakish speller"
        self.assertTrue(is_anagram(phrase1, phrase2))
        self.assertFalse(is_anagram("a b c", "a b d"))

    def test_punctation_ignored(self):
        phrase1 = "A diet"
        phrase2 = "I'd eat"
        self.assertTrue(is_anagram(phrase1, phrase2))


if __name__ == "__main__":
    unittest.main()
