'''
Unit Test cases for the ValidType, IntegerField, and CharField data Descriptors.

Test Cases:

A) Test Descriptor Init
	1) 1 of the bounds mentioned
	2) Both bounds mentioned
	3) None of the bounds mentioned

B) Test Descriptor Effectiveness
	1) Correct error raised when incorrect type recived.
	2) Correct exception raised if input is less than min (if specified)
	3) Correct exception raised if input is more than max (if specified)
	4) No exception raised if input is between min and max (if specified)

'''

import pytest
from random import randint

from Part_4.Section09_Project4.arnav_aolution import IntegerField, CharField


def _setup_wslots_(char_min=None, char_max=None, int_min=None, int_max=None):
	''' Function returns the Person class with given min and max values for CharField and IntegerField data descriptors.'''

	class Person_int:
		''' Initialises the Person class to use the IntegerField and CharField data descriptors'''
		__slots__ = ('__weakref__',)
		age = IntegerField(int_min, int_max)

		def __init__(self, age):
			self.age = age

	class Person_char:
		''' Initialises the Person class to use the IntegerField and CharField data descriptors'''
		__slots__ = ('__weakref__',)
		name = CharField(char_min, char_max)

		def __init__(self, name):
			self.name = name

	return Person_int, Person_char


# Tests for making sure the Data Descriptor Initialisation has correct inputs


##### Now for each of these tests, try to set and get and change the value and make sure things work.


@pytest.mark.parametrize('char_min, int_min, name, age', [
	(1, 0, 'a', 0), (1, 0, 'arna chdd', 10),
	(-5, -10, 'a', 0), (-5, -10, 'arna chdd', 10)
])
def test_min_only_valid(char_min, int_min, name, age):
	''' Test for when the user inputs only the min value'''

	assert _setup_wslots_(char_min=char_min, int_min=int_min)

	cls_int, cls_char = _setup_wslots_(char_min=char_min, int_min=int_min)
	assert cls_int(age), cls_char(name)

	p1_int, p1_char = cls_int(age), cls_char(name)
	assert ((p1_int.age, p1_char.name) == (age, name))

	(p1_int.age, p1_char.name) = (age + 10, name + 'random')
	assert ((p1_int.age, p1_char.name) == (age + 10, name + 'random'))


@pytest.mark.parametrize('char_min, int_min', [('1', '0'), ([1.9], [9.9]), (1 + 2j, 3 + 4j), (1.9, 9.9), (-3.4, -9.9)])
def test_min_only_invalid(char_min, int_min):
	''' Test for when the user inputs only the min value'''
	with pytest.raises(TypeError):
		assert _setup_wslots_(char_min=char_min, int_min=int_min)


@pytest.mark.parametrize('char_max, int_max, name, age', [
	(1, 0, 'a', 0), (1, 0, '', 0),
	(5, -10, 'arnav', -11)
])
def test_max_only_valid(char_max, int_max, name, age):
	''' Test for when the user inputs only the max value'''
	assert _setup_wslots_(char_max=char_max, int_max=int_max)

	cls_int, cls_char = _setup_wslots_(char_max=char_max, int_max=int_max)
	assert cls_int(age), cls_char(name)

	p1_int, p1_char = cls_int(age), cls_char(name)
	assert ((p1_int.age, p1_char.name) == (age, name))

	(p1_int.age, p1_char.name) = (age - 10, name[:-1])
	assert ((p1_int.age, p1_char.name) == (age - 10, name[:-1]))


@pytest.mark.parametrize('char_max, int_max', [('1', '0'), ([1.9], [9.9]), (1 + 2j, 3 + 4j), (1.9, 9.9), (-3.4, -9.9)])
def test_max_only_invalid(char_max, int_max):
	''' Test for when the user inputs only the max value'''
	with pytest.raises(TypeError):
		assert _setup_wslots_(char_max=char_max, int_max=int_max)


@pytest.mark.parametrize('char_min, char_max, int_min, int_max',
                         [
	                         (1, 100, -10, 20),
	                         (0, 10, 0, 0),
	                         (0, 1, 0, 0),
                         ])
def test_min_and_max_valid(char_min, char_max, int_min, int_max):
	''' Test for when the user inputs both the min and max values'''
	assert _setup_wslots_(char_min=char_min, int_min=int_min, char_max=char_max, int_max=int_max)

	cls_int, cls_char = _setup_wslots_(char_min=char_min, int_min=int_min, char_max=char_max, int_max=int_max)

	# Run the assertion tests 10 times
	for _ in range(10):
		age = randint(int_min, int_max)
		name = 'a' * randint(char_min, char_max)

		assert cls_int(age), cls_char(name)

		p1_int, p1_char = cls_int(age), cls_char(name)
		assert ((p1_int.age, p1_char.name) == (age, name))

		random_age = int((int_max + int_min)/2)
		random_name = 'a' * randint(char_min, int((char_max+char_min)/2))

		(p1_int.age, p1_char.name) = (int((int_max + int_min)/2), random_name)
		assert ((p1_int.age, p1_char.name) == (random_age, random_name))


'''
char_min, char_max, int_min, int_max, name, age
()
	(1, 100, -10, 20, 'a', 10),
	(1, 100, -10, 20, 'arnav', -10),
	(1, 100, -10, 20, 'arnav choudhury', 20),
	 


'''


def test_no_bounds():
	''' Test for when the user inputs neither the min nor the max value'''
	pass
