'''
Tests for class CPU:

'''

# TODO Try to understand how we wrote his tests and use that knowledge to write unit tests for the remaining 3 classes

from decimal import Decimal
import pytest
from Part_4.Section07_Project3.app_arnav.models.cpu import CPU

def test_class_init():
	''' Tests class Init for various success and failure cases'''

	# Success Cases
	assert CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, "AM", 15)
	assert CPU("Nvidia", "Nvidia", 0, 0, 4, "AM2", 500)
	assert CPU("Nvidia GTX", "Nvidia", 1, 0, 8, "AM4", 1415)
	assert CPU("Intel Core i9-9900K", "Intel", 10, 10, 16, "AM8", 2335)

	# Failure Cases
	with pytest.raises(ValueError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, " ", 15)

	with pytest.raises(ValueError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, "", 15)

	with pytest.raises(ValueError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, 0, "AM4", 15)

	with pytest.raises(ValueError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, "AM4", 0)

	with pytest.raises(ValueError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, "AM4", -10)

	with pytest.raises(ValueError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, -80, "AM4", 15)

	with pytest.raises(TypeError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, "AM4", Decimal('10'))

	with pytest.raises(TypeError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, 4, "AM4", '15')

	with pytest.raises(TypeError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, 2+3j, "AM4", Decimal('10'))

	with pytest.raises(TypeError):
		CPU("Intel Core i9-9900K", "Intel", 10, 0, '-80', "AM4", 15)

def test_readonly_cores():
	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, "AM", 15)
	with pytest.raises(AttributeError):
		r1.cores = 8

def test_readonly_socket():
	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, "AM", 15)
	with pytest.raises(AttributeError):
		r1.socket = "AM8"

def test_readonly_power_watts():
	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 0, 2, "AM", 15)
	with pytest.raises(AttributeError):
		r1.power_watts = 123