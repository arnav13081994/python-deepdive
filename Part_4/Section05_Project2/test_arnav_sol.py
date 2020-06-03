'''
Write tests for the following cases:

1) value is positive integral
1) value is negative integral
2) Modulus is positive integral
3) Value is positive but not integral
3) Value is negative but not integral
4) Modulus is positive but not integral
5) Modulus is negative integral
6) Modulus is negative but not integral
7) Attribute error for trying ot set either the value or the modulus of a MOD object instance
'''
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
