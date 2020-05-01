"""
Edit the parse_ranges function so that it accepts a string containing ranges of numbers and returns a generator of
the actual numbers contained in the ranges. The range numbers are inclusive.

>>> parse_ranges('0-0,4-8,20-21,43-45')
[0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]
"""




def parse_ranges(a):
    """Return a list of numbers corresponding to number ranges in a string"""

    ans = (
        range(
            int(e.split('-')[0]), 1 + int(e.split('-')[1])
        )
        for e in a.split(',')
    )
    return (j for i in ans for j in i)

