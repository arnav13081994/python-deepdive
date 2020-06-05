'''
This is the base class, Resource

Functionality:

Properties:
	name : user-friendly name of resource instance (e.g.Intel Core i9-9900K)
	manufacturer - resource instance manufacturer (e.g. Nvidia)
	total : inventory total (how many are in the inventory pool)
	allocated : number allocated (how many are already in use)
	category - computed property that returns a lower case version of the class name

Methods:
	claim(n) : method to take n resources from the pool (as long as inventory is available)
	freeup(n) : method to return n resources to the pool (e.g. disassembled some builds)
	died(n) : method to return and permanently remove inventory from the pool (e.g. they broke something) - as long as total available allows it
	purchased(n) - method to add inventory to the pool (e.g. they purchased a new CPU)

Dunders:
	a __str__ representation that just returns the resource name
	a mode detailed __repr__ implementation
'''

from numbers import Integral


def f(a, b=object):
	''' Diffrentiate between the case of the user providing None as a value and the user not providing a value at all'''
	if id(None) == id(b):
		print(f"User entered b as {b}")
	elif id(b) == id(object):
		print("User didn't enter any value for b")
	elif id(b) != id(object):
		print(f"User entered b as {b}")


class Resource:

	def __init__(self, name: str, manufacturer: str, total: int, allocated: int):

		# validations
		self.validate(name, str, min_length=1)
		self.validate(manufacturer, str, min_length=1)
		self.validate(total, Integral, min_value=0)
		self.validate(allocated, Integral, max_value=total, min_value=0)

		self._name = name.strip()
		self._manufacturer = manufacturer.strip()
		self._total = total  # Current Total
		self._allocated = allocated  # Current Allocated
		self.category = type(self).__name__.lower()

	def validate(self, arg, arg_type, max_value=None, min_value=None, min_length=None):
		'''
		 need to validate instance attribute for their type, are they between bounds (both upper and lower optional)
		 '''

		category = type(self).__name__.lower()
		if not isinstance(arg, arg_type):
			raise TypeError(f"Incorrect Type received. Expected {arg_type}")
		elif min_value is not None and arg < min_value:
			raise ValueError(f"Please stay above {min_value} {'and ' + str(max_value) if max_value is not None else ''}"
			                 f" for {category} instances.")
		elif max_value is not None and arg > max_value:
			raise ValueError(f"Please stay {'above' + str(min_value) if min_value is not None else ''} and below "
			                 f"{max_value} for {category} instances.")
		elif min_length is not None and len(arg.strip()) < min_length:
			raise ValueError(f"Please input at least {min_length} character(s) for {category} instances.")

	@property
	def allocated(self):
		return self._allocated

	@property
	def total(self):
		return self._total

	@property
	def name(self):
		return self._name

	@property
	def manufacturer(self):
		return self._manufacturer

	@allocated.setter
	def allocated(self, value):
		# if value < 0:
		# 	value = 0
		self.validate(value, Integral, max_value=self.total, min_value=0)
		self._allocated = value

	@total.setter
	def total(self, value):
		self.validate(value, Integral, min_value=0)
		self._total = value

	def claim(self, n):
		""" Will take n resources from the pool (as long as inventory is available) """
		# Check number of available resources in the pool. If sufficient then claim, and update it.

		self.validate(n, Integral, min_value=0, max_value=self.total - self.allocated)
		self.allocated += n

	def freeup(self, n):
		""" Will return n resources to the pool (e.g. disassembled some builds) """
		# Check number of available resources in the pool. If sufficient then claim, and update it.

		self.validate(n, Integral, min_value=0, max_value=self.allocated)
		self.allocated -= n

	def kill(self, n):
		'''Will return and permanently remove inventory from the pool (e.g. they broke something) - as
		 long as total available allows it and we first remove all allocated resources'''
		self.validate(n, Integral, min_value=0, max_value=self.total)
		self.total -= n
		self.freeup(n if n < self.allocated else self.allocated)

	def purchased(self, n):
		'''Will add inventory to the pool (e.g. they purchased a new CPU) '''
		self.validate(n, Integral, min_value=0)
		self.total += n

	def __str__(self):
		return self.name

	def __repr__(self):
		class_attr_dict = {k.strip('_'): v for k, v in vars(self).items()}
		return f'{self.category}({class_attr_dict})'


if __name__ == "__main__":
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 0)
	print(r1.__repr__())
	type(r1)
	print(r1.category)

