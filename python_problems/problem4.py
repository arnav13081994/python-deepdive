"""

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
# Solution #1

def twoSum(nums_list, target):
	""" Given the list of numbers and the target return the index of 2 numbers in nums_list
	that add up exactly to the target. There would be exactly 1 solution.
	"""
	# Create a dictionary where index is the key and the value is the entry in the list
	# dic = dict(zip(nums_list, range(len(nums_list))))
	dic = dict(zip(range(len(nums_list)), nums_list))
	dic_copy = dic.copy()

	for index, number in dic.items():

		tar_num = target - number
		# Now remove the number key-val from dic before checking for the key
		del dic_copy[index]

		if tar_num in dic_copy.values():

			for ind, num in dic_copy.items():
				if num == tar_num:
					return [index, ind]

		# Add back the deleted key since the value didn't match
		dic_copy[index] = number

	else:
		print("Not Found")