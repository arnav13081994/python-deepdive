'''

Please note that the user is not allowed to move money to another acocunt or to one of their own account.
So for the sake of simplicity, I am assuming one user has only 1 account.

Classes:

1) Accounts Class:

 monthly_interest_rate: CLASS ATTR,

 account_number: INST ATTR,
 current_balance: INST ATTR,
 user_first_name: INST ATTR,
 user_last_name: INST ATTR,
 time_zn_pref_offset: INST ATTR


3) Transactions Class: transaction_type_tpl, transaction_id, transaction_time_utc,
4) TimeZones Class: name, offset_hr, offset_min


Helper Methods:

1) Transaction number/status generator
2) Account number generator: Should have access to a set of all account_numbers. Checks if it is present, otherwise generates a new number and then adds to the set.
3) Monthly interest rate calculator Method
4) Pay monthly interest rate method: Given the monthly interest rate and the average monthly balance, calculates and deposits the interest and return the new balance and a transaction ID.


'''

from numbers import Integral
from datetime import timedelta


class TimeZone:

	def __init__(self, name, offset_hr, offset_min):
		print("Initialsing")
		self._name = name
		self._offset_hr = offset_hr
		self._offset_min = offset_min
		self._offset = None

	# TODO At class instance init time, setters and geters are not called. They are called when the class instance attributes are requeted or updated after clreation and initilsaition only.
	# TODO Refactor the code to have validators for offset, offset_hr, and offset_min and use them in class __init__ as well as in the 3 setters respectively.

	@property
	def name(self):
		''' a 3 letter timezone belonging to the datetime.datetime class'''
		return self._name

	@name.setter
	def name(self, value):
		""" Valid timezone name can only contain letters, has no leading or trailing spaces and is of type str"""
		print("running name setter....")

		if not isinstance(value, str):
			raise TypeError("Timezone must be of type str")
		elif not value.strip() or not value.strip().isalpha():
			raise ValueError("Timezone name cannot be empty or contain anything but letters.")
		self._name = value.strip()

	@property
	def offset_hr(self):
		''' defines the offset in hours from UTC.'''
		return self._offset_hr

	@offset_hr.setter
	def offset_hr(self, value):
		# Validate tz offset hour

		print("settings offset hour....")
		if not isinstance(value, Integral):
			raise TypeError("Hours Offset needs to be an integer")
		elif not (-12 <= value <= 14):
			raise ValueError("Hours Offset must be between -12 and +14")
		self._offset_hr = value

		# Trigger update for _offset
		self._offset = timedelta(hours=self._offset_hr)

	@property
	def offset_min(self):
		''' defines the offset in minutes from UTC.'''
		return self._offset_min

	@offset_min.setter
	def offset_min(self, value):
		# Validate the TZ offset_min
		print("settings offset minute....")
		if not isinstance(value, Integral):
			raise TypeError("Minutes Offset needs to be an integer")
		elif not (0 <= value <= 59):
			raise ValueError("Minutes Offset must be between 0 and +59. Sign of hours would be used to create"
			                 " the correct offset")
		self._offset_min = value

		# Trigger update for _offset
		self._offset = timedelta(minutes=self._offset_min)

	@property
	def offset(self):
		''' Gets the timedelta offset value'''
		return self._offset

	@offset.setter
	def offset(self, value):
		if self._offset_min and self._offset_hr:
			self._offset = timedelta(minutes=self._offset_min, hours=self._offset_hr)
		else:
			self._offset = value

	def __eq__(self, other):
		return (isinstance(other, TimeZone) and
		        self._name == other._name and
		        self._offset_hr == other._offset_hr and
		        self._offset_min == other._offset_min)

	def __repr__(self):
		return f'TimeZone(name={self._name}, offset_hr={self._offset_hr}, offset_min={self._offset_min})'


if __name__ == "__main__":
	tz1 = TimeZone('ABC', -2, -15)
	tz2 = TimeZone('ABC', -2, -15)
	print(tz1)
	print(tz1 == tz2)
	tz1.offset_hr = 10
	tz1.offset_min = 100
	print(tz1)
