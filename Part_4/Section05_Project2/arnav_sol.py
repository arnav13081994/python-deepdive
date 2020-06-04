from functools import total_ordering

@total_ordering
class Mod:
	"""
	Class mimicking Math % operator. Implements basic Modulo Arithmetic as well.
	"""
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

	def __lt__(self, other):
		'''Check if the given Mod instance's value is lower than other's or not'''
		self, other = self.conv_to_mod(other)
		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		return self.value < other.value

	def __add__(self, other):
		'''Adds and returns a new Mod instance.'''
		print("add called")
		self, other = self.conv_to_mod(other)

		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		return Mod(self.value + other.value, self.modulus)


	def __iadd__(self, other):
		'''Adds and returns a mutated Mod instance.'''
		print("iadd called")
		self, other = self.conv_to_mod(other)
		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		self._value += other.value
		self._value = self.value % self.modulus
		return self

	def __neg__(self):
		print("neg called")
		return Mod(-self.value, self.modulus)

	def __sub__(self, other):
		print("sub called")
		return self + (-other)

	def __isub__(self, other):
		print("isub called")
		self += -other
		return self

	def __mul__(self, other):
		'''Multiplies and returns a new Mod instance.'''
		print("mul called")
		self, other = self.conv_to_mod(other)

		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		return Mod(self.value * other.value, self.modulus)


	def __imul__(self, other):
		'''Multiplies and returns a mutated Mod instance.'''
		print("imul called")
		self, other = self.conv_to_mod(other)
		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		self._value *= other.value
		self._value = self.value % self.modulus
		return self


	def __pow__(self, power, modulo=None):
		''' Returns the Exponentiated version of Mod object'''
		print("pw called")
		self, power = self.conv_to_mod(power)

		if (self, power) == (NotImplemented, NotImplemented):
			return NotImplemented
		return Mod(self.value ** power.value, self.modulus)

	def __ipow__(self, other):
		print("ipow called")
		self, other = self.conv_to_mod(other)
		if (self, other) == (NotImplemented, NotImplemented):
			return NotImplemented
		self._value **= other.value
		self._value = self.value % self.modulus
		return self

	def __repr__(self):
		''' Mod object instance representation'''
		return f'Mod(value={self.value}, modulus={self.modulus})'


	def __hash__(self):
		return hash((self.value, self.modulus))

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
		print(f"Conv called {self}, {other}")

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
	print({a})