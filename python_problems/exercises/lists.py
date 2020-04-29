"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    vowel = ['a', 'e', 'i', 'o', 'u']
    return [name for name in names if name[0].lower() in vowel]


def power_list(lst):
    """Return a list that contains each number raised to the i-th power."""
    return [num**index for index, num in enumerate(lst)]


def flatten(a):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [j for i in a for j in i]


def reverse_difference(lst):
    """Return list subtracted from the reverse of itself."""
    reverse_lst = lst.copy()
    reverse_lst.reverse()
    return [a-b for a, b in zip(lst, reverse_lst)]

def matrix_add(m1, m2):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [sum(j) for j in zip(*i)]
        for i in zip(m1, m2)
    ]


def transpose():
    """Return a transposed version of given list of lists."""


def get_factors():
    """Return a list of all factors of the given number."""


def triples():
    """Return list of Pythagorean triples less than input num."""
