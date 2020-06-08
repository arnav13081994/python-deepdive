'''

Write 2 data descriptors:

1) IntegerField --> Only allows Integral numbers, between minimum and maximum value
2) CharField --> Only allows strings with a minimum and maximum length


The class that may use these 2 data descriptors may or may not use slots and may or may not be hasheable.



Structure:

1) main class --> ValidType that you can extend and define defaults of minimum and maximum lengths and value and expected types


'''

from numbers import Integral, Real
from weakref import ref
import ctypes


class ValidType:

	def __init__(self, minimum=None, maximum=None):
		assert isinstance(minimum, Real), "Minimum Value must be a Real Number"
		assert isinstance(maximum, Real), "Maximum Value must be a Real Number"
		self.minimum = minimum
		self.maximum = maximum
		self.values = {}

	def _finalise_obj(self, weakref_obj):
		''' Looks up the object that had its last strong ref removed and also removes the weak ref from the data
		descriptor instance dict.'''
		key = ''
		for k, v in self.values.items():
			if v[0] is weakref_obj:
				key = k
				break
		if key:
			del self.values[key]

	def __set_name__(self, owner, name):
		self.name = name

	def __get__(self, instance, owner):
		if instance is None:
			return self
		val = self.values.get(id(instance), None)
		if val is not None:
			return val[1]
		return val


class IntegerField(ValidType):
	''' This is a data descriptor that does validation and raises appropriate errors that doesn't assume that
	 the class that uses this has __dict__'''

	def __set__(self, instance, value):

		# Validations
		if not isinstance(value, Integral):
			raise TypeError(f'{self.name} must be of type {type(self).__name__}.')
		elif self.minimum is not None and value < self.minimum:
			raise ValueError(f'{self.name} must be greater than {self.minimum}.')
		elif self.maximum is not None and value > self.maximum:
			raise ValueError(f'{self.name} must be less than {self.maximum}.')

		self.values[id(instance)] = (ref(instance, self._finalise_obj), value)



class CharField(ValidType):
	''' This is a data descriptor that does validation and raises appropriate errors that doesn't assume that
	 the class that uses this has __dict__'''

	def __init__(self, minimum=0, maximum=None):
		minimum = minimum or 0 # In case the user enters Minimum as None
		minimum = max(minimum, 0)
		super().__init__(minimum, maximum)


	def __set__(self, instance, value):

		# Validations
		if not isinstance(value, str):
			raise TypeError(f'{self.name} must be of type {type(self).__name__}.')
		elif self.minimum is not None and len(value) < self.minimum:
			raise ValueError(f'{self.name} must have at least {self.minimum} characters.')
		elif self.maximum is not None and len(value) > self.maximum:
			raise ValueError(f'{self.name} must have fewer than {self.maximum} characters.')

		self.values[id(instance)] = (ref(instance, self._finalise_obj), value)



def get_strong_ref_ct(address):
	return ctypes.c_long.from_address(address).value


if __name__ == "__main__":
	class Person:
		''' Initialises the Person class to use the IntegerField and CharField data descriptors'''
		__slots__ = ('__weakref__',)
		name = CharField(-10, 255)
		age = IntegerField(0, 50.12)

		def __init__(self, name, age):
			self.name = name
			self.age = age


	p = Person("Arnav Choudhury", 25)

	pid = id(p)
	print(pid, get_strong_ref_ct(pid), p.name, p.age)
	p.name, p.age = "Pranav", 31
	print(pid, get_strong_ref_ct(pid), p.name, p.age)
	del p
	print(pid, get_strong_ref_ct(pid))
