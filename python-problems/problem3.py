"""
This week I'd like you to write a class representing a 3-dimensional point.

The Point class must accept 3 values on initialization (x, y, and z) and have x, y, and z attributes.
It must also have a helpful string representation.
Additionally, point objects should be comparable to each other
(two points are equal if their coordinates are the same and not equal otherwise).
"""


class Point:

	def __init__(self, x, y, z):
		self._x = x
		self._y = y
		self._z = z

	def __eq__(self, other):
		if isinstance(other, Point):
			return bool(self.x == other.x and self.y == other.y and self.z == other.z)
		return False

	def __repr__(self):
		return "Point(x={0}, y={1}, z={2})".format(self.x, self.y, self.z)

	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	@property
	def z(self):
		return self._z

	@x.setter
	def x(self, x):
		if isinstance(x, int) or isinstance(x, float):
			self._x = x
		else:
			raise ValueError("Points must be either integer or floats.")

	@y.setter
	def y(self, y):
		if isinstance(y, int) or isinstance(y, float):
			self._y = y
		else:
			raise ValueError("Points must be either integer or floats.")

	@z.setter
	def z(self, z):
		if isinstance(z, int) or isinstance(z, float):
			self._z = z
		else:
			raise ValueError("Points must be either integer or floats.")

	# Bonus: 1

	def __add__(self, other):
		if isinstance(other, Point):
			return Point(self.x + other.x, self.y + other.y, self.z + other.z)

		raise ValueError("Only 2 instances of the Points Class can be added.")

	def __sub__(self, other):
		if isinstance(other, Point):
			return Point(self.x - other.x, self.y - other.y, self.z - other.z)

		raise ValueError("Only 2 instances of the Points Class can be added.")

	# Bonus: 2

	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return Point(self.x * other, self.y * other, self.z * other)

		raise ValueError("Points can only be raised by integers or floats.")

	def __rmul__(self, other):
		if isinstance(other, int) or isinstance(other, float):
			return Point(self.x * other, self.y * other, self.z * other)

		raise ValueError("Points can only be raised by integers or floats.")

	# Bonus: 3

	def __iter__(self):
		self.iters = 0
		return self

	def __next__(self):
		iter_number = self.iters
		self.iters += 1
		if iter_number == 0:
			return self.x
		elif iter_number == 1:
			return self.y
		elif iter_number == 2:
			return self.z
		else:
			raise StopIteration
