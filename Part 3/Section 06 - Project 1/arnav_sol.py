def validate(data, template, path=[]):
	"""    implement and return True/False
    in the case of False, return a string describing
    the first error encountered
    in the case of True, string can be empty
    """
	for key, value in template.items():

		if key not in data:
			path += [key]
			return False, KeyError(f"Key: {'.'.join(path)} is not present")

		if not isinstance(value, dict):
			# This is the case of single data type checking
			if not isinstance(data[key], value):
				path += [key]
				return False, TypeError(
					f"Expected Type: {value} for key: {'.'.join(path)}. Received: {type(data[key])}")
		elif isinstance(value, dict):

			path += [key]
			state, error = validate(data[key], value, path=path)
			if not state:
				return state, error
			else:
				path.pop()

	return True, ''


if __name__ == "__main__":
	data = {
		'user_id': 102,
		'name': {
			'first': 'Michael',
			'last': 'Palin'
		},
		'bio': {
			'dob': {
				'year': 1943,
				'month': 'May',
				'day': 5
			},
			'birthplace': {
				'country': 'United Kingdom',
				'city': 'Sheffield'
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
