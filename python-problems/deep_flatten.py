def deep_flatten(matrix_lst):
	"""
	Will take in a list of iterables and return a flattened iterable
	"""
	from collections.abc import Iterable
	for matrix in matrix_lst:

		if isinstance(matrix, Iterable) and not isinstance(matrix, str):
			yield from deep_flatten(matrix)

		else:
			yield matrix


if __name__ == "__main__":
	lst = [
		[(1, 2), (3, 4)],
		[(5, 6), (7, 8)]
	]

	ans = deep_flatten(lst)
	print(ans)

	while True:
		print(next(ans))
