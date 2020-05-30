def validate(data, template, path=[]):
	"""    implement and return True/False
    in the case of False, return a string describing
    the first error encountered
    in the case of True, string can be empty
    """
	for key, value in template.items():

		if key not in data:
			raise KeyError(f"Key: {'.'.join(path + [key])} is not present")

		if not isinstance(value, dict) and not isinstance(data[key], value):
			raise TypeError(
				f"Expected Type: {value} for key: {'.'.join(path + [key])}. Received: {type(data[key])}")

		if isinstance(value, dict):
			validate(data[key], value, path=path + [key])

	return True, ''


if __name__ == "__main__":
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
	john = {
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
	michael = {
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
	eric = {
		'user_id': 101,
		'name': {
			'first': 'Eric',
			'last': 'Idle'
		},
		'bio': {
			'dob': {
				'year': 1943,
				'month': 3,
				'day': 29
			},
			'birthplace': {
				'country': 'United Kingdom'
			}
		}
	}

	print(validate(john, template))
	print(validate(eric, template))
	print(validate(michael, template))
