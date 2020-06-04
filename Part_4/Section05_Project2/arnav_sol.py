'''



Implement  +, -, *, ** as well as equivalent in place operations

All math operations between 2 mod will only happen if they have the same modulus, in case one of them is an integer convert the int to basically an equivalent MNod object with the same modulus
And the operators will always return a MOD instance.

Same as above except that the operators now are in-place
Implement +, -, *, ** as well as a method so that calling int(mod_object) will return the residue.

All math operatoins between 2 mod will only happen if they have the same modulus, in case one of them is an integer convert the int to basically an equivalent MNod object with the same modulus
And the operators will always return a MOD instance.

Implement ordering and compare using value of the Mod. Support comprison between 2 mod objects (same modulus) as well as a mod object and an int.

'''
from functools import total_ordering

class Mod:

	def __init__(self, value, modulus):
		self._modulus = self.validate_modulus(modulus)
		self._value = self.validate_value(value) % self._modulus

	@property
	def modulus(self):
		''' modulus of the MOD object instance'''
		return self._modulus

	@property
	def value(self):
		''' value of the MOD object instance'''
		return self._value

	def __int__(self):
		return self.value

	def __eq__(self, other):
		'''Checks if the value of Mod is the same or not.'''
		self, other = self.conv_to_mod(other)
		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		return self.value == other.value

	def __add__(self, other):
		'''Adds and returns a new Mod instance.'''
		print(f"add called, {self}, {other} ")
		self, other = self.conv_to_mod(other)
		print(f"add called, {self}, {other} ")
		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		return Mod(self.value + other.value, self.modulus)

	def __radd__(self, other):
		'''Adds and returns a new Mod instance'''
		print("radd called ")
		return self.__add__(other)

	def __iadd__(self, other):
		'''Adds and returns a mutated Mod instance.'''
		print("iadd called ")
		self, other = self.conv_to_mod(other)
		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		self._value += other.value
		self._value = self.value % self.modulus
		return self



	def __sub__(self, other):
		print("sub called")
		pass

	def __isub__(self, other):
		pass

	def __mul__(self, other):
		print("mul called")
		pass

	def __imul__(self, other):
		pass

	def __pow__(self, power, modulo=None):
		print("pw called")
		pass

	def __repr__(self):
		''' Mod object instance representation'''
		return f'Mod(value={self.value}, modulus={self.modulus})'


	# Helper Functions
	def validate_modulus(self, value):

		if not isinstance(value, int):
			raise TypeError("Modulus must be an integer")
		elif value <= 0:
			raise ValueError("Modulus must be a positive integer")
		return value


	def validate_value(self, value):

		if not isinstance(value, int):
			raise TypeError("Value must be an integer")
		return value

	def conv_to_mod(self, other):
		''' Returns (self, other) Mod instances with the same moduli, if possible.
		 Otherwise return (NotImplemented, NotImplemented)'''

		print(f'{self}, {other}')

		# If other is anything but not int or Mod object return NotImplemented
		if isinstance(other, Mod) or isinstance(other, int):
			# Check that the 2 Mod objects have the same modulus otherwise raise NotImplemented
			if isinstance(other, Mod):
				if self.modulus != other.modulus:
					return NotImplemented, NotImplemented
				else:
					return self, other
			else:
				# Convert other to Mod object
				return self, Mod(other, self.modulus)
		return NotImplemented, NotImplemented


if __name__ == "__main__":

	a = Mod(8, 3)
	d = Mod(11, 3)
	b = 11
	c = 12
	print(a == Mod(8,5))
	# print((2+3j) + (Mod(10, 10)))
	# print(('2+3j') + (Mod(10, 10)))
	# print("10.3" + Mod(10,  10))
	#
	# print(hex(id(a)))
	# print(hex(id(d)))
	# e = 11 + a
	# print(hex(id(e)))
	# print(e)
	#
	# a += d
	# print(hex(id(a)))
	# print(a)

	# print(hex(id(a)))
	# print(hex(id(b)))
	# b += a
	# print(b)
	# print(hex(id(b)))
	#
	#
	# b = 11
	# print(hex(id(b)))
	# print(hex(id(a)))
	# a += b
	# print(a)
	# print(hex(id(a)))
	#
