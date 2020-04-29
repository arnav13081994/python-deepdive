def get_words_reg_back(lst):
	""" Given an array of words, return the subset of words of length 5
	 ST the reverse of that word is also a word. Words can be repeated as well."""

	lst_new = [word for word in lst if len(word) >= 5]
	lst_new = list(set(lst_new))

	# Now you have the list with unique 5 letter words
	return [word for word in lst_new if word[::-1] in lst_new]