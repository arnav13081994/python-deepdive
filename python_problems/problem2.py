"""

Write an effecient function that can take any number of points in k dimensional space and return the distance of that
point from a given point in k dimensional space.

"""


def find_dist_btw_2pts(point, origin, exp=0.5):
	""" Given a point and origin in n dimensoinal space, returns the euclidena distance between the 2"""

	return sum(map(lambda x, y: (x - y) ** 2, point, origin)) ** exp
