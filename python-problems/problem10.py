

'''
Write a function that takes one required positional and 1 optional keyword arguement with default of None.
Print the value of the optional keyword argument that the user enters. If the user doesn't enter any value for it,
print that the user chose not to enter any valye for the keyword argument.

'''


def f(a, b=object):
	''' Diffrentiate between the case of the user providing None as a value and the user not providing a value at all'''
	if b is None:
		print(f"User entered b as {b}")
	elif b is object:
		print("User didn't enter any value for b. Default value used.")
	elif b is not object:
		print(f"User entered b as {b}")
