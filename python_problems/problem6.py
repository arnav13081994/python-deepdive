def get_words_reg_back(lst):
	""" Given an array of words, return the subset of words of length 5
	 ST the reverse of that word is also a word. Words can be repeated as well."""

	set_new = set(
		word for word in lst if len(word) >= 5
	)

	return [word for word in set_new if word[::-1] in set_new]
