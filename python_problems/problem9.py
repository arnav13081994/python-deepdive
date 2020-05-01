"""
Given a list of numbers and a target sum, return all quadruples that add up to that sum

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


