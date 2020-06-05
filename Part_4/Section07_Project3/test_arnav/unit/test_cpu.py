'''
Tests for class CPU:

 1) Ensure CPU initialisation works as expected
 2) Ensure cores, socket, and power_watts are read only attributes
 3) Make sure that the validator methods validate correctly.
 4) Test claim
 5) Test kill
 6) Test freeup
 7) Test purchase
 8) Make sure total attribute gets updated correctly
 9) Make sure allocated attribute gets updated correctly

'''


# TODO Write Unit tests for CPU Class
# TODO Run Baptiste's Unit tests for CPU Class and correct any mistakes
# TODO Run Baptiste's Unit tests for CPU Class and correct any mistakes
# TODO Try to understand how we wrote his tests and use that knowledge to write uint tests for the remaining 3 classes

from decimal import Decimal
import pytest
from Part_4.Section07_Project3.app_arnav.models.resource import CPU

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



# def test_claim():
# 	''' Tests the claim method of CPU Class'''
# 	### Check Independent Updates
#
# 	# Success Cases
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 2)
# 	r1.claim(5)
# 	assert r1.allocated == 7
#
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 6)
# 	r1.claim(4)
# 	assert r1.allocated == 10
#
#
# 	# Failure Cases
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 0).claim(-1)
#
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 0).claim(11)
#
# 	with pytest.raises(TypeError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 0).claim(1.58)
#
# 	with pytest.raises(TypeError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 0).claim('11')
#
# 	### Check Chained Updates (since this method mutates self)
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 2)
#
# 	r1.claim(1)
# 	assert r1.allocated == 3
#
# 	r1.claim(2)
# 	assert r1.allocated == 5
#
# 	with pytest.raises(ValueError):
# 		r1.claim(6)
#
# def test_freeup():
# 	''' Tests the freeup method of CPU Class'''
# 	### Check Independent Updates
#
# 	# Success Cases
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 7)
# 	r1.freeup(5)
# 	assert r1.allocated == 2
#
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 6)
# 	r1.freeup(6)
# 	assert r1.allocated == 0
#
# 	# Failure Cases
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 7).freeup(-1)
#
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 7).freeup(8)
#
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 7).freeup(10)
#
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 7).freeup(12)
#
# 	with pytest.raises(TypeError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 7).freeup(1.58)
#
# 	with pytest.raises(TypeError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 7).freeup('11')
#
# 	### Check Chained Updates (since this method mutates self)
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 7)
#
# 	r1.freeup(5)
# 	assert r1.allocated == 2
#
# 	r1.freeup(1)
# 	assert r1.allocated == 1
#
# 	with pytest.raises(ValueError):
# 		r1.freeup(5)
#
# def test_kill():
# 	''' Tests the kill method of CPU Class'''
# 	### Check Independent Updates
#
# 	# Success Cases
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 7)
# 	r1.kill(5)
# 	assert r1.total == 5
#
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 6)
# 	r1.kill(2)
# 	assert r1.total == 8
#
# 	# Failure Cases
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 6).kill(-1)
#
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 6).kill(11)
#
# 	with pytest.raises(TypeError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 6).kill(1.58)
#
# 	with pytest.raises(TypeError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 6).kill('11')
#
#
# 	### Check Chained Updates (since this method mutates self)
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 7)
#
# 	r1.kill(5)
# 	assert r1.total == 5
#
# 	r1.kill(1)
# 	assert r1.total == 4
#
# 	with pytest.raises(ValueError):
# 		r1.kill(5)
#
# def test_purchased():
# 	''' Tests the purchase method of CPU Class'''
# 	### Check Independent Updates
#
# 	# Success Cases
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 7)
# 	r1.purchased(5)
# 	assert r1.total == 15
#
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 6)
# 	r1.purchased(0)
# 	assert r1.total == 10
#
# 	# Failure Cases
# 	with pytest.raises(ValueError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 6).purchased(-1)
#
# 	with pytest.raises(TypeError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 6).purchased(1.58)
#
# 	with pytest.raises(TypeError):
# 		CPU("Intel Core i9-9900K", "Intel", 10, 6).purchased('11')
#
# 	### Check Chained Updates (since this method mutates self)
# 	r1 = CPU("Intel Core i9-9900K", "Intel", 10, 6)
#
# 	r1.purchased(5)
# 	assert r1.total == 15
#
# 	r1.purchased(2)
# 	assert r1.total == 17
#
