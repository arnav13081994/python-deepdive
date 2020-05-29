def validate(data, template):
	"""    implement and return True/False
    in the case of False, return a string describing
    the first error encountered
    in the case of True, string can be empty

    """

	for key, value in template.items():

		if key not in data:
			return False, KeyError(f"Key: {key} is not present")

		if not isinstance(value, dict):
			# This is the case of single data type checking
			if not isinstance(data[key], value):  # value != type(data[key]):
				return False, TypeError(f"Expected Type: {value} for key: {key}. Received: {type(data[key])}")
		elif isinstance(value, dict):

			state, error = validate(data[key], value)
			if not state:
				return state, error

	return True, ''


if __name__ == "__main__":
	data = {
		'user_id': 100,
		'name': {
			'first': 'John',
			'last': 'Cleese'
		},
		'bio': {
			'dob': {
				'year': 1939,
				'month': 11,
				'day': 27
			},
			'birthplace': {
				'country': 'United Kingdom',
				'city': 'Weston-super-Mare'
			}
		}
	}

	template = {
		'user_id': int,
		'name': {
			'first': str,
			'last': str
		},
		'bio': {
			'dob': {
				'year': int,
				'month': int,
				'day': int
			},
			'birthplace': {
				'country': str,
				'city': str
			}
		}
	}
	print(validate(data, template))
