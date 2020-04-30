"""More comprehension exercises"""


def flip_dict(dic):
    """Return a new dictionary that maps the original values to the keys."""
    return {val: key for key, val in dic.items()}
def get_ascii_codes(words):
    """Return a dictionary mapping the strings to ASCII codes."""
def dict_from_truple(list):
    """Turn three-item tuples into a dictionary of two-valued tuples."""

    return {i: tuple(j) for i, *j in list}
def dict_from_tuple(list):
    """Turn multi-item tuples into a dictionary of two-valued tuples."""
    return {i: tuple(j) for i, *j in list}
def get_factors(number):
    """Get factors of the given number."""
    return (
        n
        for n in range(1, number + 1)
        if number % n == 0
    )
def get_all_factors(set_num):
    """Return a dictionary mapping numbers to their factors."""
    return {num: list(get_factors(num)) for num in set_num}
