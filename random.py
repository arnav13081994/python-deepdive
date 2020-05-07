# use fn.__code__.co__freevars: for free variable tuple
# use fn.__closure__ for the shared cell tuple info.


def dec_fact1(a, b):
	def dec(f):
		def inner(*args, **kwargs):
			print("About to run the function {0} and {1}".format(a, b))
			return f(*args, **kwargs)

		return inner

	return dec


def add(a, b):
	return a + b


class dec_fact:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __call__(self, f):
		def inner(*args, **kwargs):
			print("About to run the function {0} and {1}".format(self.a, self.b))
			return f(*args, **kwargs)

		return inner


if __name__ == "__main__":
	add = dec_fact(10, 20)(add)
	print(add(1, 5))
