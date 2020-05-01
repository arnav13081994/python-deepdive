"""


Edit the triples function so that it takes a number and returns a list of tuples of 3 integers where each tuple is a
Pythagorean triple, and the integers are all less then the input number.
A Pythagorean triple is a group of 3 integers a, b, and c, such that they satisfy the formula a**2 + b**2 = c**2

"""



def twosum(lst, target_sum):
    """ Given a list of numbers and a target sum, return all doubles that add up to that sum"""

    return [
        [i, target_sum - i]
        for i in lst
        if (target_sum - i) in lst and i != (target_sum - i)
    ]


def triples_v2(num):
    """Return list of Pythagorean triples less than input num."""
    lst = [i ** 2 for i in range(1, num)]
    ans = []

    # Now the question essentially is to find 3 numbers ST 2 of them add up to the third one.
    for num in lst:
        target_sum = num
        candidate_lstoflists = twosum(lst, target_sum)
        for i in candidate_lstoflists:
            i += [num]
            ans.append(i)

    ans = return_unique_members(ans)
    ans = [tuple([int(e**0.5) for e in lst]) for lst in ans]
    return ans


def return_unique_members(lst):
    """ Given an iterable  of tuples, return only unique tuples.
    Uniqueness is defined if no 2 tuples have all the same elements. Order doesn't matter"""

    ans = []
    set_unique = set()
    for i in lst:
        if not set(i).issubset(set_unique):
            #  Add all elements of that tuple to ans
            set_unique.update(i)
            ans.append(i)
    return ans



