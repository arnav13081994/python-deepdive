


def time_it(fn, *args, **kwargs):
	""" Returns the time taken to run the function"""

	t0 = time.time()

	# Execute the function
	fn(*args, **kwargs)

	t1 = time.time()
	time = t1-t0

	return time





# Question: https://www.pythonmorsels.com/exercises/cb8fbdd52cf14f8cb31df4f06343cccf/



def add(*matrices):
	""" Given n matrices of the same size this function will do an elementwise addition
	 and return the nex matrix
	 """
	from functools import reduce

	# Check if all matrices have the same shape, if not return ValueError
	matrix_len_lst = [all([len(matrix[0]) == len(element) for element in matrix]) for matrix in matrices]
	# have the same number of elements

	matrix_len_lst2 = [len(matrices[0]) == len(matrix) for matrix in matrices]

	if all(matrix_len_lst) and all(matrix_len_lst2):
		return reduce(add_ind_mat, matrices)
	raise ValueError("Given matrices are not the same size.")


def add_ind_mat(mat1, mat2):
	""" Takes 2 matrices and returns a matrix obtained by doing elementwise addition."""

	tup_iterator = zip(mat1, mat2)
	lst2 = []
	for i in tup_iterator:
		unrolled_mat = zip(*i)
		lst = []
		for matrix in unrolled_mat:
			lst.append(sum(matrix))

		lst2.append(lst)

	return lst2













