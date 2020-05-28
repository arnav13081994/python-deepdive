import csv
import os
from collections import namedtuple
import datetime
from itertools import groupby, islice

file_names = (

	'employment.csv',
	'personal_info.csv',
	'update_status.csv',
	'vehicles.csv',
)


def file_iter(file_name):
	file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)

	with open(file_path) as f:
		file_reader = csv.reader(f)
		yield from clean_data(file_reader)


def clean_data(file_iter):
	data = []
	header = next(file_iter)
	data_tup = namedtuple('Data', header)
	for row in file_iter:
		row = data_tup(*cast_data(row, header))
		data.append(row)
	yield data


def cast_data(row, header):
	data_lst = []

	for data, data_type in zip(row, header):
		if data_type == 'last_updated' or data_type == 'created':
			(date, time) = data.split('T')
			(y, m, d) = date.split('-')
			(h, minute, s) = time.split(':')
			data = datetime.datetime(int(y), int(m), int(d), int(h), int(minute), int(s[:-1]))
		elif data_type == 'model_year':
			data = datetime.datetime(int(data), 1, 1)  # Defaulting to Jan 1 of that year for the car model

		else:
			data = str(data)

		data_lst.append(data)
	return data_lst


if __name__ == "__main__":
	data = []
	dic = dict()

	for f_name in file_names:
		data.extend(next(file_iter(f_name)))

	# Sort data by ssn for groupby to work properly
	data.sort(key=lambda x: x.ssn)

	# We need to refer to the ssn field in the big lst data and then groupby on that as key and combine them all into
	# another iterable.
	grouped = groupby(data, key=lambda x: x.ssn)

	data = []
	print(hex(id(data)))
	for key, groups in grouped:

		for group in groups:
			dic = {**dic, **group._asdict()}

		tup = namedtuple('DATA', list(dic.keys()))
		data.append(tup(**dic))


	for ind, dat in enumerate(data):
		print(f"row:{ind+1}, {dat}")



# TODO Another algo specifically for goal 2.

# 1) Go through every file and just get the heads and combine them into a list and create a numed tuple. Easy way would to combine all heads, convert into set and then back.
	# Also make sure to keep track of individual heads in each file as that would be used to make sure the final named tuple has correct data entered.
	# Also use the defaults parameter = (None, ) * len(headers) to create defaults for other values that would eventually get filled.
# 2) Since csv.reader returns an iterator we can just pick up where we left off.
# 3) Now, iterate over the rows of ery file and check if an entry for that ssn in the data lst of named tuples exists or not, if exists update it, otherwise add it!
# 4) Repeat step 3) for all files.
# 5) Time approach #1 and approach #2 and see if the second approach is faster or not and what's the RAM footprint.



file_names = (

	'employment.csv',
	'personal_info.csv',
	'update_status.csv',
	'vehicles.csv',
)
