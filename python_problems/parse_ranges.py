"""
Edit the parse_ranges function so that it accepts a string containing ranges of numbers and returns a generator of
the actual numbers contained in the ranges. The range numbers are inclusive.

>>> parse_ranges('0-0,4-8,20-21,43-45')
[0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45]
"""

# TODO Try to use th ecsv module instead of a.split to see if you can lazy loop and split the input string.




def parse_ranges(a):
    csv_reader = csv.reader([a])

    """Return a list of numbers corresponding to number ranges in a string"""
    for row in csv_reader:
        for group in row:
            start, sep, end = group.partition('-')
            if end.startswith('>') or not sep:
                yield int(start)
            else:
                yield from range(int(start), int(end)+1)


def parse_ranges_a(a):
    """Return a list of numbers corresponding to number ranges in a string"""
    for group in a.split(','):
        start, sep, end = group.partition('-')
        if end.startswith('>') or not sep:
            yield int(start)
        else:
            yield from range(int(start), int(end)+1)

if __name__ == "__main__":
    import csv
    from time import perf_counter
    a = '0-0,4-8,20-21,43-45,'

    # Create a very long random string
    b = a * 2000000
    b = b[:-1]


    t0 = perf_counter()
    q = parse_ranges_a(b)
    while True:
        try:
            next(q)
        except Exception as e:
            t1 = perf_counter()
            print("Time Taken:", (t1-t0)/len(b))
            break

    t0 = perf_counter()
    q = parse_ranges(b)
    while True:
        try:
            next(q)
        except Exception as e:
            t1 = perf_counter()
            print("Time Taken by with csv:", (t1-t0)/len(b))
            break






