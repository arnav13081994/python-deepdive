'''
Test Cases:

1) Expected Exceptions for invalid Mod.value and Mod.modulus attrs.
2) Expected Exceptions for trying to set read-only Mod.value and Mod.modulus attrs.
3) Expected Behaviour for valid Mod.value and Mod.modulus attrs.
4) Expected Exceptions for invalid Mod object comparison.
5) Expected Behaviour for valid Mod object comparison.

'''

'''
Congruence test cases:



'''


from decimal import Decimal
import pytest
from Part_4.Section05_Project2.arnav_sol import Mod


# Helper Function
def is_mod(value, modulus):
	''' Returns True if it is a valid mod instance, otherwise False'''

	try:
		if Mod(value, modulus):
			return True
	except Exception as e:
		return False


# Tests for expected Happy Cases for Mod Object Initialisation
def test_mod_happy():
	assert is_mod(10, 10) == True
	assert is_mod(-10, 10) == True
	assert is_mod(0, 10) == True


# Validating Expected Exceptions
def test_validate_modulus_exceptions():
	''' Tests for Expected Validation Exceptions raised with the error messages specifically for Modulus instance attr'''

	with pytest.raises(ValueError) as exec_info:
		Mod(10, -10)
	assert str(exec_info.value) == 'Modulus must be a positive integer'

	with pytest.raises(ValueError) as exec_info:
		Mod(10, 0)
	assert str(exec_info.value) == 'Modulus must be a positive integer'

	with pytest.raises(TypeError) as exec_info:
		Mod(10, "-10")
	assert str(exec_info.value) == 'Modulus must be an integer'

	with pytest.raises(TypeError) as exec_info:
		Mod(10, 10.9)
	assert str(exec_info.value) == 'Modulus must be an integer'

def test_validate_value_exceptions():
	with pytest.raises(TypeError) as exec_info:
		Mod("10", 10)
	assert str(exec_info.value) == 'Value must be an integer'

	with pytest.raises(TypeError) as exec_info:
		Mod(10.9, 10)
	assert str(exec_info.value) == 'Value must be an integer'

def test_read_only_exceptions():
	with pytest.raises(AttributeError):
		a = Mod(10, 10)
		a.value = 15

	with pytest.raises(AttributeError):
		a = Mod(10, 10)
		a.modulus = 15


# Dunder Method Test Cases
def test_eq_happy():

	# Comparison of 1 Mod object with not an int
	assert Mod(10, 10).__eq__(10.3) == NotImplemented
	assert 10.3.__eq__(Mod(10, 10)) == NotImplemented
	assert Mod(10, 10).__eq__('10.3') == NotImplemented
	assert "10.3".__eq__(Mod(10, 10)) == NotImplemented
	assert Mod(10, 10).__eq__(Decimal('10.3')) == NotImplemented
	assert Decimal('10.3').__eq__(Mod(10, 10)) == NotImplemented
	assert Mod(10, 10).__eq__(2+3j) == NotImplemented
	assert (2+3j).__eq__(Mod(10, 10)) == NotImplemented


	# Comparison of 1 mod object with an int
	assert Mod(10, 10).__eq__(0) == True
	assert Mod(8, 3).__eq__(11) == True
	assert Mod(8, 3).__eq__(10) == False


	# Comparison of 2 Mod objects with different moduli
	assert Mod(10, 10).__eq__(Mod(10, 7)) == NotImplemented
	assert Mod(110, 20).__eq__(Mod(10, 30)) == NotImplemented

	# Comparison of 2 Mod objects with same moduli

	# Success
	assert Mod(-115, 20).__eq__(Mod(25, 20)) == True
	assert Mod(11, 3).__eq__(Mod(8, 3)) == True

	# Failure
	assert Mod(110, 20).__eq__(Mod(-33, 20)) == False
	assert Mod(-115, 20).__eq__(Mod(-25, 20)) == False
