"""

Given a list of integers,  a target sum, return all unique sub-arrays of the given size.


"""
def return_unique_members(lst):
	""" Given an iterable  of tuples, return only unique tuples.
    Uniqueness is defined if no 2 tuples have all the same elements. Order doesn't matter"""

	ans = []
	set_unique = set()
	for i in lst:
		if not set(i).issubset(set_unique):
			#  Add all elements of that tuple to ans
			set_unique.update(i)
			ans.append(i)
	return ans

def twosum(lst, target_sum):
	""" Given a list of numbers and a target sum, return all doubles that add up to that sum"""

	ans = [
		[num, target_sum - num]
		for num in lst
		if (target_sum - num) in lst and num != (target_sum - num)
	]

	return ans

def threesum(lst, target_sum):
	"""Given a list of numbers and a target sum, return all triples that add up to that sum"""

	ans = [
		i + [num]
		for num in lst
		for i in twosum(lst, target_sum - num)
	]

	return ans

# TODO Need ot debug. For some reason it is not working properly for size > 6. Either throws an error or returns the wrong answer.

def ksum(lst, target_sum, target_size):
	"""Given a list of numbers and a target sum, return all quadruples that add up to that sum"""

	for num in lst:
		target_size -= 1
		target_sum -= num
		print("Target Size:", target_size, "Target Sum:", target_sum, "Target Num:", num, "list:", lst)

		if target_size == 3:
			ans = [lst + [num] for lst in threesum(lst, target_sum)]
			print("Ans for size 3:", ans)
			return ans
		else:
			ans = [lst + [num] for lst in ksum(lst, target_sum, target_size)]
			ans = return_unique_members(ans)  # Remove duplicate iterables in the list
			ans = [tuple(lst) for lst in ans]  # Convert the iterables in the list to tuples
			return ans


def ksum_v2(lst, target_sum, target_size):
	"""Given a list of numbers and a target sum, return all quadruples that add up to that sum"""

	for num in lst:
		target_size -= 1
		target_sum -= num

		if target_size == 2:
			ans = [lst + [num] for lst in twosum(lst, target_sum)]
			return ans
		else:
			ans = [lst + [num] for lst in ksum(lst, target_sum, target_size)]
			ans = return_unique_members(ans)  # Remove duplicate iterables in the list
			ans = [tuple(lst) for lst in ans]  # Convert the iterables in the list to tuples
			return ans


if __name__ == "__main__":
	print('starting')
	a = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
	target_sm = 0
	target_sz = 8
	print(return_unique_members(ksum(a, target_sm, target_sz)))
