


def time_it(fn, *args, **kwargs):
	""" Returns the time taken to run the function"""

	t0 = time.time()

	# Execute the function
	fn(*args, **kwargs)

	t1 = time.time()
	time = t1-t0

	return time



