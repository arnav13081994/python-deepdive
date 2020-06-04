'''
Test Cases:

1) Expected Exceptions for invalid Mod.value and Mod.modulus attrs.
2) Expected Exceptions for trying to set read-only Mod.value and Mod.modulus attrs.
3) Expected Behaviour for valid Mod.value and Mod.modulus attrs.
4) Expected Exceptions for invalid Mod object comparison.
5) Expected Behaviour for valid Mod object comparison.
6) Expected Exceptions for invalid Mod object addition.
7) Expected Behaviour for valid Mod object addition.


'''

'''
add test cases:
1) 2 mod objects are added with the same moduli
2) 2 mod objects are added with different moduli
3) 1 mod objects is added to an int
4) 1 mod objects is added to not an int


iadd test cases:

1) Same as add test cases except that self needs to be mutated and returned in each case.


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


def id_same(obj1, obj2, operator):
	''' Returns True if both the objects pased have the same ID'''
	# This will either throw an exception depending on what obj2 is
	obj3 = obj1
	if operator == "+=":
		obj1 += obj2
	elif operator == "-=":
		obj1 -= obj2
	elif operator == "*=":
		obj1 *= obj2

	return obj1 is obj3


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
	assert Mod(10, 10) != 10.3
	assert Mod(10, 10) != '10.3'
	assert Mod(10, 10) != Decimal('10.3')
	assert Mod(10, 10) != 2 + 3j

	# Comparison of 1 mod object with an int
	assert Mod(10, 10) == 0
	assert Mod(8, 3) == 11
	assert Mod(8, 3) != 10

	# Comparison of 2 Mod objects with different moduli
	assert Mod(10, 10) != Mod(10, 7)
	assert Mod(110, 20) != Mod(10, 30)

	# Comparison of 2 Mod objects with same moduli

	# Success
	assert (Mod(-115, 20) == Mod(25, 20))
	assert (Mod(11, 3) == Mod(8, 3))

	# Failure
	assert (Mod(110, 20) != Mod(-33, 20))
	assert (Mod(-115, 20) != Mod(-25, 20))



# '+' and '+=' test cases
def test_add_happy():

	# Addition of 1 Mod object with not an int
	with pytest.raises(TypeError):
		Mod(10, 10) + 10.3
	with pytest.raises(TypeError):
		Mod(10, 10) + '10.3'
	with pytest.raises(TypeError):
		Mod(10, 10) + Decimal('10.3')
	with pytest.raises(TypeError):
		Mod(10, 10) + (2+3j)


	# Addition of 1 mod object with an int
	assert Mod(10, 10) + 0 == Mod(10, 10)
	assert Mod(8, 3) + 11 == Mod(19, 3)
	assert Mod(8, 3) + 10 == Mod(18, 3)


	# Addition of 2 Mod objects with different moduli
	with pytest.raises(TypeError):
		Mod(10, 10) + Mod(10, 7)
	with pytest.raises(TypeError):
		Mod(110, 20) + Mod(10, 30)

	# Addition of 2 Mod objects with same moduli

	# Success
	assert Mod(-115, 20) + Mod(15, 20) == Mod(-100, 20)
	assert Mod(11, 3) + Mod(8, 3) == Mod(19, 3)

	# Failure
	assert Mod(110, 20) + Mod(-33, 20) != Mod(-115, 20)
	assert Mod(-115, 20) + Mod(-25, 20) != Mod(-115, 20)
def test_iadd_happy():
	''' Tests in place addition operators which needs to return the same hex(id(Mod))'''

	# Addition of 1 Mod object with not an int
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), 10.3, '+=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), '10.3', '+=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), Decimal('10.3'), '+=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), (2+3j), '+=')


	# Addition of 1 mod object with an int
	assert id_same(Mod(10, 10), 0, '+=')
	assert id_same(Mod(8, 3), 11, '+=')
	assert id_same(Mod(8, 3), 10, '+=')


	# Addition of 2 Mod objects with different moduli
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), Mod(10, 7), '+=')
	with pytest.raises(TypeError):
		id_same(Mod(110, 20), Mod(10, 30), '+=')


	# Addition of 2 Mod objects with same moduli

	# Success
	assert id_same(Mod(-115, 20), Mod(15, 20), '+=')
	assert id_same(Mod(11, 3), Mod(8, 3), '+=')

	# Failure
	assert id_same(Mod(110, 20), Mod(-33, 20), '+=')
	assert id_same(Mod(-115, 20), Mod(-25, 20), '+=')


# '-' and '-=' test cases
def test_sub_happy():

	# Addition of 1 Mod object with not an int
	with pytest.raises(TypeError):
		Mod(10, 10) - 10.3
	with pytest.raises(TypeError):
		Mod(10, 10) - '10.3'
	with pytest.raises(TypeError):
		Mod(10, 10) - Decimal('10.3')
	with pytest.raises(TypeError):
		Mod(10, 10) - (2+3j)


	# Addition of 1 mod object with an int
	assert Mod(10, 10) - 0 == Mod(10, 10)
	assert Mod(8, 3) - 11 == Mod(-3, 3)
	assert Mod(8, 3) - 10 == Mod(-2, 3)


	# Addition of 2 Mod objects with different moduli
	with pytest.raises(TypeError):
		Mod(10, 10) - Mod(10, 7)
	with pytest.raises(TypeError):
		Mod(110, 20) - Mod(10, 30)

	# Addition of 2 Mod objects with same moduli

	# Success
	assert Mod(-115, 20) - Mod(15, 20) == Mod(-130, 20)
	assert Mod(11, 3) - Mod(8, 3) == Mod(3, 3)

	# Failure
	assert Mod(110, 20) - Mod(-33, 20) != Mod(-115, 20)
	assert Mod(-115, 20) - Mod(-25, 20) != Mod(-115, 20)
def test_isub_happy():
	''' Tests in place subtraction operators which needs to return the same hex(id(Mod))'''

	# Addition of 1 Mod object with not an int
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), 10.3, '-=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), '10.3', '-=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), Decimal('10.3'), '-=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), (2+3j), '-=')


	# Addition of 1 mod object with an int
	assert id_same(Mod(10, 10), 0, '-=')
	assert id_same(Mod(8, 3), 11, '-=')
	assert id_same(Mod(8, 3), 10, '-=')


	# Addition of 2 Mod objects with different moduli
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), Mod(10, 7), '-=')
	with pytest.raises(TypeError):
		id_same(Mod(110, 20), Mod(10, 30), '-=')


	# Addition of 2 Mod objects with same moduli

	# Success
	assert id_same(Mod(-115, 20), Mod(15, 20), '-=')
	assert id_same(Mod(11, 3), Mod(8, 3), '-=')

	# Failure
	assert id_same(Mod(110, 20), Mod(-33, 20), '-=')
	assert id_same(Mod(-115, 20), Mod(-25, 20), '-=')


# '*' and '*=' test cases
def test_mul_happy():

	# Addition of 1 Mod object with not an int
	with pytest.raises(TypeError):
		Mod(10, 10) * 10.3
	with pytest.raises(TypeError):
		Mod(10, 10) * '10.3'
	with pytest.raises(TypeError):
		Mod(10, 10) * Decimal('10.3')
	with pytest.raises(TypeError):
		Mod(10, 10) * (2+3j)


	# Addition of 1 mod object with an int
	assert Mod(10, 10) * 0 == Mod(0, 10)
	assert Mod(8, 3) * 11 == Mod(88, 3)
	assert Mod(8, 3) * 10 == Mod(80, 3)


	# Addition of 2 Mod objects with different moduli
	with pytest.raises(TypeError):
		Mod(10, 10) * Mod(10, 7)
	with pytest.raises(TypeError):
		Mod(110, 20) * Mod(10, 30)

	# Addition of 2 Mod objects with same moduli

	# Success
	assert Mod(-115, 20) * Mod(15, 20) == Mod(-115*15, 20)
	assert Mod(11, 3) * Mod(8, 3) == Mod(88, 3)

	# Failure
	assert Mod(110, 20) * Mod(-33, 20) != Mod(0, 20)
	assert Mod(-115, 20) * Mod(-25, 20) != Mod(20, 20)
def test_imul_happy():
	''' Tests in place subtraction operators which needs to return the same hex(id(Mod))'''

	# Addition of 1 Mod object with not an int
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), 10.3, '*=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), '10.3', '*=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), Decimal('10.3'), '*=')
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), (2+3j), '*=')


	# Addition of 1 mod object with an int
	assert id_same(Mod(10, 10), 0, '*=')
	assert id_same(Mod(8, 3), 11, '*=')
	assert id_same(Mod(8, 3), 10, '*=')


	# Addition of 2 Mod objects with different moduli
	with pytest.raises(TypeError):
		id_same(Mod(10, 10), Mod(10, 7), '*=')
	with pytest.raises(TypeError):
		id_same(Mod(110, 20), Mod(10, 30), '*=')


	# Addition of 2 Mod objects with same moduli

	# Success
	assert id_same(Mod(-115, 20), Mod(15, 20), '*=')
	assert id_same(Mod(11, 3), Mod(8, 3), '*=')

	# Failure
	assert id_same(Mod(110, 20), Mod(-33, 20), '*=')
	assert id_same(Mod(-115, 20), Mod(-25, 20), '*=')
