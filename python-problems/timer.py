def time_it(fn, *args, n=1000, **kwargs):
	""" Returns the average time taken to run the function n times"""
	import time
	t0 = time.time()

	# Execute the function n times
	for i in range(n):
		fn(*args, **kwargs)

	t1 = time.time()
	time = t1 - t0

	return time/n