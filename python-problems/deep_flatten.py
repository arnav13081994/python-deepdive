from collections.abc import Iterable

def deep_flatten(matrix_itr):
	"""
	Will take in an Iterable of iterables and returns a flattened iterable
	"""
	for matrix in matrix_itr:
		if isinstance(matrix, Iterable) and not isinstance(matrix, str):
			yield from deep_flatten(matrix)
		else:
			yield matrix


if __name__ == "__main__":
	lst = [
		[(1, 2), [(3, '4', 'arnav')]],
		[('5', 6), [(7, ['8'])]]
	]

	print(list(deep_flatten(lst)))
