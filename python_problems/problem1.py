"""
Question: https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/

"""

# Solution #1

def raise_ValError():
	raise ValueError("Given matrices are not the same size.")


def add(*matrices_tuple):
	""" Given n matrices of the same size this function will do an elementwise addition
	 and return the nex matrix
	 """
	from functools import reduce

	# We not only need to check that the 2 lists have the same number of matrices but also that every matrix has the same
	# number of elements at the corresponding locations in the list of lists passed

	matrix_len_lst = [

		all([
			(
					len(matrix_of_matrix[0]) == len(element)
					and len(matrices_tuple[0]) == len(matrix_of_matrix) or raise_ValError()
			)
			for element in matrix_of_matrix
		])

		for matrix_of_matrix in matrices_tuple
	]

	if all(matrix_len_lst):
		return reduce(add_ind_mat_v1, matrices_tuple)
	raise_ValError()


def add_ind_mat_v1(mat1, mat2):
	""" Takes 2 matrices and returns a matrix obtained by doing elementwise addition."""
	lst2 = []

	for i in zip(mat1, mat2):
		# Unzip so that you get the new matrix that have corresponding elements together!
		lst = []

		for matrix in zip(*i):
			lst.append(sum(matrix))

		lst2.append(lst)

	return lst2


# Solution #2


def add_ind_mat_v2(mat1, mat2):
	""" Takes 2 matrices and returns a matrix obtained by doing elementwise addition."""

	lst = [
		[
			k+j for k, j in zip(*i)
		]
		for i in zip(mat1, mat2)
	]

	return lst


# Solution #3







# Benchmark Results
from python_problems.timer import time_it


time_it(print, 'abc', n=5)
