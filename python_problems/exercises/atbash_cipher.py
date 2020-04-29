# MIT Licensed
# https://github.com/exercism/python/blob/master/LICENSE
from string import ascii_lowercase as letters


atbash = dict(zip(letters, reversed(letters)))


def decode(string):
    """Return string of each character decoded."""


def encode(string):
    """Decode each letter and group into 5-letter words."""
