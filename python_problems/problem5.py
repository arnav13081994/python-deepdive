#  TODO Refactor this entire file using the code written for Problem7


# TODO Come up with a solution that works for k numbers. Probably use recursion. Divide and conquer.
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
		print("Index: ", index, "Number:", num, "Target Sum:", target_sum_new, "Target Size:", target_size_new, "List:",
		      nums_lst_new)

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
