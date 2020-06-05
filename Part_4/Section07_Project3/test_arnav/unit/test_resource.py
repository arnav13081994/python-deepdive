'''
Tests for base class Resource:

 ###### 1) Ensure Resource initialisation works as expected
 ###### 2) Ensure name, and manufacturer are read only attributes
 ###### 3) Make sure that the validator methods validate correctly.
 ###### 4) Test claim
 ###### 5) Test kill
 ###### 6) Test freeup
 ###### 7) Test purchase
 ###### 8) Make sure total attribute gets updated correctly
 ###### 9) Make sure allocated attribute gets updated correctly

'''

from decimal import Decimal
import pytest
from Part_4.Section07_Project3.app_arnav.models.resource import Resource

def test_class_init():
	''' Tests class Init for various success and failure cases'''

	# Success Cases
	assert Resource("Intel Core i9-9900K", "Intel", 10, 0)
	assert Resource("Nvidia", "Nvidia", 0, 0)
	assert Resource("Nvidia GTX", "Nvidia", 1, 0)
	assert Resource("Intel Core i9-9900K", "Intel", 10, 10)

	# Failure Cases
	with pytest.raises(ValueError):
		Resource("", "", 10, 0)

	with pytest.raises(ValueError):
		Resource("Nvidia", " ", 10, 0)

	with pytest.raises(ValueError):
		Resource("Nvidia GTX", "", 10, 0)

	with pytest.raises(ValueError):
		Resource("", "Nvidia", 10, 0)

	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 15)

	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", -10, 0)

	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, -1)

	with pytest.raises(TypeError):
		Resource(12, "Intel", 10, 15)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", 14+3j, -10, 0)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", '10', 1)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, -1+3j)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", Decimal('10'), 5)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10.5, 5)

def test_readonly_name():
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 0)
	with pytest.raises(AttributeError):
		r1.name = "NVIDIA GTX=1080"

def test_readonly_manufacturer():
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 0)
	with pytest.raises(AttributeError):
		r1.manufacturer = "NVIDIA"

def test_claim():
	''' Tests the claim method of Resource Class'''
	### Check Independent Updates

	# Success Cases
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 2)
	r1.claim(5)
	assert r1.allocated == 7

	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 6)
	r1.claim(4)
	assert r1.allocated == 10


	# Failure Cases
	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 0).claim(-1)

	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 0).claim(11)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, 0).claim(1.58)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, 0).claim('11')

	### Check Chained Updates (since this method mutates self)
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 2)

	r1.claim(1)
	assert r1.allocated == 3

	r1.claim(2)
	assert r1.allocated == 5

	with pytest.raises(ValueError):
		r1.claim(6)

def test_freeup():
	''' Tests the freeup method of Resource Class'''
	### Check Independent Updates

	# Success Cases
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 7)
	r1.freeup(5)
	assert r1.allocated == 2

	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 6)
	r1.freeup(6)
	assert r1.allocated == 0

	# Failure Cases
	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 7).freeup(-1)

	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 7).freeup(8)

	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 7).freeup(10)

	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 7).freeup(12)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, 7).freeup(1.58)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, 7).freeup('11')

	### Check Chained Updates (since this method mutates self)
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 7)

	r1.freeup(5)
	assert r1.allocated == 2

	r1.freeup(1)
	assert r1.allocated == 1

	with pytest.raises(ValueError):
		r1.freeup(5)

def test_kill():
	''' Tests the kill method of Resource Class'''
	### Check Independent Updates

	# Success Cases
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 7)
	r1.kill(5)
	assert r1.total == 5

	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 6)
	r1.kill(2)
	assert r1.total == 8

	# Failure Cases
	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 6).kill(-1)

	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 6).kill(11)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, 6).kill(1.58)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, 6).kill('11')


	### Check Chained Updates (since this method mutates self)
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 7)

	r1.kill(5)
	assert r1.total == 5

	r1.kill(1)
	assert r1.total == 4

	with pytest.raises(ValueError):
		r1.kill(5)

def test_purchased():
	''' Tests the purchase method of Resource Class'''
	### Check Independent Updates

	# Success Cases
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 7)
	r1.purchased(5)
	assert r1.total == 15

	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 6)
	r1.purchased(0)
	assert r1.total == 10

	# Failure Cases
	with pytest.raises(ValueError):
		Resource("Intel Core i9-9900K", "Intel", 10, 6).purchased(-1)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, 6).purchased(1.58)

	with pytest.raises(TypeError):
		Resource("Intel Core i9-9900K", "Intel", 10, 6).purchased('11')

	### Check Chained Updates (since this method mutates self)
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 6)

	r1.purchased(5)
	assert r1.total == 15

	r1.purchased(2)
	assert r1.total == 17

