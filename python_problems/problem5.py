def threeSum(nums):
	"""
	Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
	 Find all unique triplets in the array which gives the sum of zero.

	Note:

	The solution set must not contain duplicate triplets.


	:param nums:
	:return:
	"""
	list_of_lists = []
	set_to_check = set()
	lst_searched = nums.copy()
	index = -1

	for num in nums:
		index += 1
		target_sum = -num

		del lst_searched[index]

		lst = twoSum(nums_list=lst_searched, target=target_sum)
		print("Target Sum:", target_sum, "; lst is:", lst)

		lst_searched.insert(index, num)

		if lst:
			lst.append(num)
			set2 = set(lst)
			print("set2: ", set2)
			if not set2.issubset(set_to_check):
				list_of_lists.append(lst)
				set_to_check = set_to_check.union(set2)

	return list_of_lists


def twoSum(nums_list, target):
	""" Given the list of numbers and the target return the 2 numbers in nums_list
	that add up exactly to the target. There can be more than 1 solution.
	"""

	if not len(nums_list) >= 2:
		return []

	lst_checked = []

	for number in nums_list:
		to_find = target - number

		if to_find in lst_checked:
			return [number, to_find]

		else:
			lst_checked.append(number)
	else:
		return []


# Come up with a solution that works for k numbers. Probably use recursion. Divide and conquer.
#   Base cases: k=0, k=1, k=2, O(n) <= n**2 where n are the number of elements in the array.


# you need to find all unique triplets of K numbers such that their sum == 0, given an array of n integers.

lst = []
def find_unique_arrangements(nums_lst: list, target_sum: int, target_size: int):
	""" Given a list of n integeres and a target sum and a target_size, find all unique subarrays of size, target_size,
	 such that the sum of their elements is equal to the target sum."""

	nums_lst_new = nums_lst.copy()
	index = -1
	print("lst is:", lst)

	for num in nums_lst:
		index += 1
		target_sum_new = target_sum - num
		del nums_lst_new[index]
		target_size_new = target_size - 1
		print("Index: ", index, "Number:", num, "Target Sum:", target_sum_new, "Target Size:", target_size_new, "List:", nums_lst_new )

		if target_size_new == 1:
			if target_sum_new in nums_lst_new:
				print("Base Case Reached")
				print("Element:", [target_sum_new])
				return lst.append(target_sum_new)
			else:
				print("Nothing found")
				return []
		else:
			ans = find_unique_arrangements(nums_lst_new, target_sum_new, target_size_new)
			nums_lst_new.insert(index, num)
			return lst.append(ans)


if __name__ == "__main__":
	print('starting')
	a = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
	target_sm = 0
	target_sz = 3

	print(find_unique_arrangements(a, target_sm, target_sz))
	# print(threeSum(a))
