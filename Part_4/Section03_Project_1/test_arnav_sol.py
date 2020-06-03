import pytest
import coverage
import tox

from numbers import Integral
from datetime import timedelta, datetime

from Part_4.Section03_Project_1.arnav_sol import TimeZone



'''
What all unit tests I would need to write:

1) TimeZone Class

A) offset_min Validation runs as expected for "happy" cases.
B) offset_hr Validation runs as expected for "happy" cases.
C) offset_name Validation runs as expected for "happy" cases. 
D) offset_min Validation fails as expected for "unhappy" cases.
E) offset_hr Validation fails as expected for "unhappy" cases.
F) offset_name Validation fails as expected for "unhappy" cases. 
G) the offset gets set up correctly when all validations pass.
H) offset throws nameerror for not being defined if 1 or more validations fail.

'''

# @pytest.mark.parametrize("maybe_valid_TimeZones, expected_result", [
#
# 	('', True),
#
#
# ])


timezone = TimeZone('abc', 2, 15)
print(timezone)

def test_always_true():
	assert True



def test_always_false():
	assert False