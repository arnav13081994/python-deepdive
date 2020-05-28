def sort_dict_by_val(d, reverse=False):
	return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))
def func(d1, d2):
	common_keys_set = d1.keys() & d2.keys()
	return dict((k, (d1[k], d2[k])) for k in common_keys_set)
def combine_dicts(*dictionaries):
	''' Receives n number of dicts and retrns a sortted combined dictioanry where
	the values are sorted in descendnig order by frequncy'''
	d = dictionaries[0]
	for dic in dictionaries[1:]:
		for k, v in dic.items():
			d[k] = d.get(k, 0) + v

	return sort_dict_by_val(d, reverse=True)
def get_data(*dicts):
	d = dicts[0]

	union_keys = set(d.keys()).union(*dicts[1:])
	intersection_keys = set(d.keys()).intersection(*dicts[1:])
	common_keys = union_keys - intersection_keys
	result = dict.fromkeys(common_keys)

	for key in common_keys:
		tup = ()
		for dic in dicts:
			tup += (dic.get(key, 0),)

		result[key] = tup
