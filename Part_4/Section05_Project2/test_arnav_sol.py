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


1) comparison of 2 mod objects with same modulus
#####2) comparison of 2 mod objects with different modulus
3) comparison of 1 mod object with an integer
#####4) comparison of 1 mod object with not an integer

create instance method for the congreunce operator ie a == b should check that a (mod n) == b (mod n) but
also allow the same comparison for int objects
eg  Mod(value, modulus) == Int => Mod(value, modulus) == Mod(int, modulus)
Allow comparison of 2 Mod objects iff they have the same modulus.

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

	# Comparison of 2 Mod objects with different moduli
	assert Mod(10, 10).__eq__(Mod(10, 7)) == NotImplemented



# TODO Find an easy way to simulate numbers that are not of type int


'''
2 mod objects with the same mod or comparison of 1 mod object and an int type
'''

#
#
# def test_eq_happy():
# 	pass

'''
Comparison of 2 mod objects with differnt modulii and comparison of a Mod object with something that is not an int.
'''