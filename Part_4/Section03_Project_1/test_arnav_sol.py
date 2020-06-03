import pytest
import coverage
import tox

from numbers import Integral
from datetime import timedelta, datetime

from Part_4.Section03_Project_1.arnav_sol import TimeZone


# TODO Come back and write tests for the Timezone class.
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
I) The sign of offset_hr and offset_min always match.

'''

# @pytest.mark.parametrize("maybe_valid_TimeZones, expected_result", [
#
# 	('', True),
#
#
# ])


timezone = TimeZone('abc', 2, 15)
print(timezone)

pytest.raises(TypeError, test_validate_offset_min, timezone=timezone)
pytest.raises(ValueError, test_validate_offset_min, timezone=timezone)


def test_validate_offset_min(timezone):

	# Try to set the offset_min value to something that is not an integer
	value = timezone._offset_min

	# Try to set the offset_min value to something that is out of the range -59 to +59
	if not isinstance(value, Integral):
		raise TypeError("Minutes Offset needs to be an integer")
	elif not (-59 <= value <= 59):
		raise ValueError(
			"Minutes Offset must be between -59 and +59. Sign of hours offset would be used to create the correct offset"
		)
	sign_hr = 1 if timezone._offset_hr >= 0 else -1
	sign_min = 1 if value >= 0 else -1

	if sign_hr == sign_min:
		return value
	return -1 * value


def test_validate_offset_hr(self, value):
	if not isinstance(value, Integral):
		raise TypeError("Hours Offset needs to be an integer")
	elif not (-12 <= value <= 14):
		raise ValueError("Hours Offset must be between -12 and +14")
	return value


def test_validate_name(self, value):
	if not isinstance(value, str):
		raise TypeError("Timezone must be of type str")
	elif not value.strip() or not value.strip().isalpha():
		raise ValueError("Timezone name cannot be empty or contain anything but letters.")
	return value.strip()

