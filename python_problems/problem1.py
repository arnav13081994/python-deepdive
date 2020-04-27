"""
Question: https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/

"""

# Solution #1
def add(*matrices_tuple):
	""" Given n matrices of the same size this function will do an elementwise addition
	 and return the nex matrix
	 """
	from functools import reduce

	# We not only need to check that the 2 lists have the same number of matrices but also that every matrix has the same
	# number of elements at the corresponding locations in the list of lists passed
	matrix_len_lst = [

		all([
			(len(matrix_of_matrix[0]) == len(element) and len(matrices_tuple[0]) == len(matrix_of_matrix))
			for element in matrix_of_matrix
		])

		for matrix_of_matrix in matrices_tuple
	]

	if all(matrix_len_lst):
		return reduce(add_ind_mat, matrices_tuple)
	raise ValueError("Given matrices are not the same size.")


def add_ind_mat(mat1, mat2):
	""" Takes 2 matrices and returns a matrix obtained by doing elementwise addition."""

	tup_iterator = zip(mat1, mat2)

	lst2 = []
	for i in tup_iterator:
		# Unzip so that you get the new matrix that have corresponding elements together!
		unzipped_mat = zip(*i)

		lst = []
		for matrix in unzipped_mat:
			lst.append(sum(matrix))

		lst2.append(lst)

	return lst2


# Solution #2






# Solution #3







# Benchmark Results
from python_problems.timer import time_it


time_it(print, 'abc', n=5)
