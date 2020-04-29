from collections import namedtuple
from textwrap import dedent
import unittest

from helpers import make_file


from advanced import (matrix_from_string, get_cards, shuffle_cards, deal_cards,
                      parse_csv)


class MatrixFromStringTests(unittest.TestCase):

    """Tests for matrix_from_string."""

    def test_two_by_two_matrix(self):
        matrix = matrix_from_string("1 2\n10 20")
        self.assertEqual([[1, 2], [10, 20]], matrix)

    def test_three_by_two_matrix(self):
        matrix = matrix_from_string("9 8 7\n19 18 17")
        self.assertEqual([[9, 8, 7], [19, 18, 17]], matrix)


class GetCardsTest(unittest.TestCase):

    """Tests for get_cards."""

    def test_get_cards(self):
        Card = namedtuple('Card', 'rank suit')

        deck = [Card(rank='A', suit='spades'), Card(rank='2', suit='spades'),
                Card(rank='3', suit='spades'), Card(rank='4', suit='spades'),
                Card(rank='5', suit='spades'), Card(rank='6', suit='spades'),
                Card(rank='7', suit='spades'), Card(rank='8', suit='spades'),
                Card(rank='9', suit='spades'), Card(rank='10', suit='spades'),
                Card(rank='J', suit='spades'), Card(rank='Q', suit='spades'),
                Card(rank='K', suit='spades'), Card(rank='A', suit='hearts'),
                Card(rank='2', suit='hearts'), Card(rank='3', suit='hearts'),
                Card(rank='4', suit='hearts'), Card(rank='5', suit='hearts'),
                Card(rank='6', suit='hearts'), Card(rank='7', suit='hearts'),
                Card(rank='8', suit='hearts'), Card(rank='9', suit='hearts'),
                Card(rank='10', suit='hearts'), Card(rank='J', suit='hearts'),
                Card(rank='Q', suit='hearts'), Card(rank='K', suit='hearts'),
                Card(rank='A', suit='diamonds'), Card(rank='2', suit='diamonds'),
                Card(rank='3', suit='diamonds'), Card(rank='4', suit='diamonds'),
                Card(rank='5', suit='diamonds'), Card(rank='6', suit='diamonds'),
                Card(rank='7', suit='diamonds'), Card(rank='8', suit='diamonds'),
                Card(rank='9', suit='diamonds'), Card(rank='10', suit='diamonds'),
                Card(rank='J', suit='diamonds'), Card(rank='Q', suit='diamonds'),
                Card(rank='K', suit='diamonds'), Card(rank='A', suit='clubs'),
                Card(rank='2', suit='clubs'), Card(rank='3', suit='clubs'),
                Card(rank='4', suit='clubs'), Card(rank='5', suit='clubs'),
                Card(rank='6', suit='clubs'), Card(rank='7', suit='clubs'),
                Card(rank='8', suit='clubs'), Card(rank='9', suit='clubs'),
                Card(rank='10', suit='clubs'), Card(rank='J', suit='clubs'),
                Card(rank='Q', suit='clubs'), Card(rank='K', suit='clubs')]

        self.assertEqual(get_cards(), deck)


class ShuffleTest(unittest.TestCase):

    """Test for shuffle_cards."""

    def test_shuffle(self):
        things = [1, 2, 3, 4, 5]
        original = list(things)
        shuffle_cards(things)
        self.assertNotEqual(original, things)
        self.assertEqual(set(original), set(things))


class DealCardsTest(unittest.TestCase):

    """Test for deal_cards."""

    def test_deal_cards(self):
        Card = namedtuple('Card', 'rank suit')
        deck = [Card(rank='A', suit='spades'), Card(rank='2', suit='spades'),
                Card(rank='3', suit='spades'), Card(rank='4', suit='spades'),
                Card(rank='5', suit='spades'), Card(rank='6', suit='spades'),
                Card(rank='7', suit='spades'), Card(rank='8', suit='spades'),
                Card(rank='9', suit='spades'), Card(rank='10', suit='spades'),
                Card(rank='J', suit='spades'), Card(rank='Q', suit='spades'),
                Card(rank='K', suit='spades'), Card(rank='A', suit='hearts'),
                Card(rank='2', suit='hearts'), Card(rank='3', suit='hearts'),
                Card(rank='4', suit='hearts'), Card(rank='5', suit='hearts'),
                Card(rank='6', suit='hearts'), Card(rank='7', suit='hearts'),
                Card(rank='8', suit='hearts'), Card(rank='9', suit='hearts'),
                Card(rank='10', suit='hearts'), Card(rank='J', suit='hearts'),
                Card(rank='Q', suit='hearts'), Card(rank='K', suit='hearts'),
                Card(rank='A', suit='diamonds'), Card(rank='2', suit='diamonds'),
                Card(rank='3', suit='diamonds'), Card(rank='4', suit='diamonds'),
                Card(rank='5', suit='diamonds'), Card(rank='6', suit='diamonds'),
                Card(rank='7', suit='diamonds'), Card(rank='8', suit='diamonds'),
                Card(rank='9', suit='diamonds'), Card(rank='10', suit='diamonds'),
                Card(rank='J', suit='diamonds'), Card(rank='Q', suit='diamonds'),
                Card(rank='K', suit='diamonds'), Card(rank='A', suit='clubs'),
                Card(rank='2', suit='clubs'), Card(rank='3', suit='clubs'),
                Card(rank='4', suit='clubs'), Card(rank='5', suit='clubs'),
                Card(rank='6', suit='clubs'), Card(rank='7', suit='clubs'),
                Card(rank='8', suit='clubs'), Card(rank='9', suit='clubs'),
                Card(rank='10', suit='clubs'), Card(rank='J', suit='clubs'),
                Card(rank='Q', suit='clubs'), Card(rank='K', suit='clubs')]
        hand = [Card(rank='K', suit='clubs'), Card(rank='Q', suit='clubs'),
                Card(rank='J', suit='clubs'), Card(rank='10', suit='clubs'),
                Card(rank='9', suit='clubs')]
        self.assertEqual(deal_cards(deck), hand)


class ParseCSVTests(unittest.TestCase):

    """Tests for parse_csv."""

    def test_sample_file(self):
        csv_data = dedent("""
            col1,col2,more_data
            1,2,3
            "a,b","c\td","e f"
        """).lstrip()
        with make_file(csv_data) as filename:
            with open(filename) as csv_file:
                csv_rows = list(parse_csv(csv_file))
        self.assertEqual(len(csv_rows), 2)
        row1, row2 = csv_rows
        self.assertEqual(row1.col1, '1')
        self.assertEqual(row1.col2, '2')
        self.assertEqual(row1.more_data, '3')
        self.assertEqual(row1, ('1', '2', '3'))
        self.assertEqual(row2, ('a,b', 'c\td', 'e f'))

    def test_state_capitals(self):
        with open('us-state-capitals.csv') as capitals_file:
            csv_rows = list(parse_csv(capitals_file))
        self.assertEqual(len(csv_rows), 50)
        self.assertEqual(csv_rows[0].state, 'Alabama')
        self.assertEqual(csv_rows[0].capital, 'Montgomery')
        self.assertEqual(csv_rows[0], ('Alabama', 'Montgomery'))


if __name__ == '__main__':
    unittest.main()
