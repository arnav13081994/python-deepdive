from collections import defaultdict, Counter
from itertools import chain, repeat


# Using Default dict
def merge_defdict(*dicts):
	'''
	Merges all passed in dicts and increases the frequency of keys and returns the sorted version back
	'''

	sorted_dic = defaultdict(int)
	for dic in dicts:
		for k, v in dic.items():
			sorted_dic[k] += v

	sorted_dic = dict(sorted(sorted_dic.items(), key=lambda x: x[1], reverse=True))
	return sorted_dic


# Using Counter object
def merge_counter_v1(*dicts):
	'''
	Merges all passed in dicts and increases the frequency of keys and returns the sorted version back
	'''

	c = Counter()
	for dic in dicts:
		c.update(dic)
	return dict(c.most_common())


# Using Counter and chain and repeat
def merge_counter_v2(*dicts):
	'''
	Merges all passed in dicts and increases the frequency of keys and returns the sorted version back
	'''
	p = (repeat(*item) for dic in dicts for item in dic.items())
	return dict(Counter(chain.from_iterable(p)).most_common())


if __name__ == "__main__":
	d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
	d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
	d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
	print(merge_defdict(d1, d2, d3))
	print(merge_counter_v1(d1, d2, d3))
	print(merge_counter_v2(d1, d2, d3))
