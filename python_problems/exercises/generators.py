"""Generator Exercises."""


def is_prime(num):
    """Return True if candidate number is prime."""
    return all(num % n for n in range(2, num))
def first_prime_over(num):
    """Return the first prime number over a given number."""
    # According to Bertrand postulate there will exist a prime number b/w n and 2n
    lst = (number for number in range(num + 1, 2 * num + 1))
    for number in lst:
        if is_prime(number):
            return number
def first_prime_over_v2(num):
    """Return the first prime number over a given number."""
    number = num + 1
    while number > num:
        if is_prime(number):
            return number
        number += 1
def all_together(*args):
    """String together all items from the given iterables."""
    # Needs to return a generator exp.
    return (e for iterable in args for e in iterable)
def is_anagram(w1, w2):
    """Return True if the given words are anagrams."""
    """ Spaces, case need to be ignored. Lengths need to be the same"""
    punct = ["'", ".", "!", "?", ",", ":", ";", " "]
    w1 = [w.lower() for w in w1 if w not in punct]
    w2 = [w.lower() for w in w2 if w not in punct]

    if len(w1) != len(w2):
        return False

    longer = w1
    shorter = w2

    for letter in shorter:
        if letter not in longer:
            return False
    else:
        return True
def interleave(l1, l2):
    """Return iterable of one item at a time from each list."""
    return (ee for e in zip(l1, l2) for ee in e)
def translate():
    """Return a transliterated version of the given sentence."""


def parse_ranges():
    """Return a list of numbers corresponding to number ranges in a string"""


