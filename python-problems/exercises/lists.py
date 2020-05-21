"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    vowel = ['a', 'e', 'i', 'o', 'u']
    return [name for name in names if name[0].lower() in vowel]
def power_list(lst):
    """Return a list that contains each number raised to the i-th power."""
    return [num ** index for index, num in enumerate(lst)]
def flatten(a):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""
    return [j for i in a for j in i]
def reverse_difference(lst):
    """Return list subtracted from the reverse of itself."""
    return [a - b for a, b in zip(lst, lst[::-1])]
def matrix_add(m1, m2):
    """Add corresponding numbers in given 2-D matrices."""
    return [
        [sum(j) for j in zip(*i)]
        for i in zip(m1, m2)
    ]
def transpose(matrix):
    """Return a transposed version of given list of lists."""
    return [list(mat) for mat in zip(*matrix)]
def get_factors(n):
    """Return a list of all factors of the given number."""
    return [number for number in range(1, n + 1) if not n % number]

def triples_v1(num):
    """Return list of Pythagorean triples less than input num."""
    # lst_seen = []
    ans = []
    lst = [i ** 2 for i in range(1, num)]
    for i in lst:
        # Now the question is the same thing as saying find 2 numbers from the list
        # S.T the square of their sum == i**2
        for j in lst:
            if j != i:
                to_find = (i - j) ** 0.5
                try:
                    if to_find == int(to_find):
                        to_find = int(to_find)
                        if bool(to_find in lst and to_find != i and to_find != j):
                            ans.append([i, j, to_find])
                except Exception as e:
                    continue

    return ans
