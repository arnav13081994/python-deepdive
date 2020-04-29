"""Advanced exercises"""
from collections import namedtuple
import csv

import random


def matrix_from_string(string):
    """Convert rows of numbers to list of lists."""


def parse_csv(file_obj):
    """Return namedtuple list representing data from given file object."""
    csv_reader = csv.reader(file_obj)
    Row = namedtuple('Row', next(csv_reader))


def get_cards():
    """Create a list of namedtuples representing a deck of playing cards."""
    Card = namedtuple('Card', 'rank suit')
    ranks = ['A'] + [] + ['J', 'Q', 'K']
    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    return [Card('A', 'spades')]


def shuffle_cards(deck):
    """Shuffles a list in-place"""
    random.shuffle(deck)


def deal_cards(deck, count=5):
    """Remove the given number of cards from the deck and returns them"""
