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

	# ans = return_unique_members(ans)  # Remove duplicate iterables in the list
	# ans = [tuple(lst) for lst in ans]  # Convert the iterables in the list to tuples
	return ans


def foursum(lst, target_sum):
	"""Given a list of numbers and a target sum, return all quadruples that add up to that sum"""

	ans = [
		i + [num]
		for num in lst
		for i in threesum(lst, target_sum - num)
	]

	ans = return_unique_members(ans)  # Remove duplicate iterables in the list
	ans = [tuple(lst) for lst in ans]  # Convert the iterables in the list to tuples
	return ans




def find_unique_arrangements(nums_lst: list, target_sum: int, target_size: int):
	""" Given a list of n integers and a target sum and a target_size, find all unique subarrays of size, target_size,
     such that the sum of their elements is equal to the target sum."""

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


if __name__ == "__main__":
	print('starting')
	a = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
	target_sm = 0
	# target_sz = 3
	print(foursum(a, target_sm))
	# print(find_unique_arrangements(a, target_sm, target_sz))

# TODO Come up with a solution that works for k numbers. Probably use recursion. Divide and conquer.
#   Base cases: k=0, k=1, k=2, O(n) <= n**2 where n are the number of elements in the array. You need to find all unique triplets of K numbers such that their sum == 0, given an array of n integers.

# lst = []
#
# def find_unique_arrangements(nums_lst: list, target_sum: int, target_size: int):
# 	""" Given a list of n integers and a target sum and a target_size, find all unique subarrays of size, target_size,
# 	 such that the sum of their elements is equal to the target sum."""
#
# 	nums_lst_new = nums_lst.copy()
# 	index = -1
# 	print("lst is:", lst)
#
# 	for num in nums_lst:
# 		index += 1
# 		target_sum_new = target_sum - num
# 		del nums_lst_new[index]
# 		target_size_new = target_size - 1
# 		print("Index: ", index, "Number:", num, "Target Sum:", target_sum_new, "Target Size:", target_size_new, "List:",
# 		      nums_lst_new)
#
# 		if target_size_new == 1:
# 			if target_sum_new in nums_lst_new:
# 				print("Base Case Reached")
# 				print("Element:", [target_sum_new])
# 				return lst.append(target_sum_new)
# 			else:
# 				print("Nothing found")
# 				return []
# 		else:
# 			ans = find_unique_arrangements(nums_lst_new, target_sum_new, target_size_new)
# 			nums_lst_new.insert(index, num)
# 			return lst.append(ans)
