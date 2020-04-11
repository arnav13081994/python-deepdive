# Implement a class Rectangle with getter and setter methods and also implement
# class instance methods like
	# area,
	# perimeter,
	# initialisatoin,
	# getter,
	# setter,
	# less than or equal to methods as well.


class Rectangle:

	@property
	def width(self):
		""" Gets the width"""
		return self._width

	@property
	def height(self):
		""" Gets the height"""
		return self._height


	def __init__(self, height, width):
		""" Initialises an instance of the Rectangle Class"""

		# _width and _height are internal (private) Rectangle Instance's attributes. This is something
		# We keep to ourselves to make sure the User can't just update these attrs randomly and also
		# so that the code has backward compatibility.
		self._width = None
		self._height = None

		# Lets now use the SETTER Method the width and height of the newly initialised Rectangle Class
		self.width = width
		self.height = height


	@width.setter
	def width(self, width):
		""" Sets the Width"""
		if width <= 0:
			raise ValueError("Width should be Positive")
		self._width = width


	@height.setter
	def height(self, height):
		""" Sets the Height"""
		if height <= 0:
			raise ValueError("Height should be Positive")
		self._height = height
