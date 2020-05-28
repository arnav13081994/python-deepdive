import csv
import datetime
import os
from collections import namedtuple
import tracemalloc
from timeit import timeit
from functools import partial
from itertools import islice, groupby

file_names = (

	'employment.csv',
	'personal_info.csv',
	'update_status.csv',
	'vehicles.csv',
)


def file_iter(file_name):
	file_path = os.path.join(os.path.dirname(__file__), 'data', file_name)
	with open(file_path) as f:
		file_reader = csv.DictReader(f)
		yield from clean_data(file_reader)


def clean_data(file_iter):
	""""""
	global data_dic
	for row in file_iter:
		row = cast_data(row)  # This will get back the cleaned and correct format data.
		try:
			data_dic[row['ssn']] = {**data_dic[row['ssn']], **row}

		except KeyError:
			# This means that this is the first time this SSN will be encountered
			data_dic[row['ssn']] = row

	# stats = tracemalloc.take_snapshot().statistics('lineno')
	# print(stats[0].size / 1024, 'kb')

	yield data_dic


def cast_data(row):
	""" Will return an instance of OrderedDict like it was passed."""

	for key, value in row.items():

		if key == 'last_updated' or key == 'created':
			(date, time) = value.split('T')
			(y, m, d) = date.split('-')
			(h, minute, s) = time.split(':')
			value = datetime.datetime(int(y), int(m), int(d), int(h), int(minute), int(s[:-1]))

		elif key == 'model_year':
			value = datetime.datetime(int(value), 1, 1)  # Defaulting to Jan 1 of that year for the car model

		else:
			value = str(value)

		row[key] = value
	return row


def run(file_names):
	data = []
	for file_name in file_names:
		next(file_iter(file_name))

	for ssn, row in data_dic.items():
		# Note in python 3, dict.items() is a view and is evaluated lazily.
		try:
			data.append(tup(**row))
		except NameError:
			tup = namedtuple('Tup', list(row.keys()))
	return data


def return_records_after(data, date):
	""" All records that have been updated after date will be returned"""

	# Convert date into datetime object and filter the data
	(m, d, y) = date.split('/')
	date = datetime.datetime(int(y), int(m), int(d))

	return data.last_updated > date


if __name__ == "__main__":
	tracemalloc.start()

	data_dic = {}
	print(timeit('data = run(file_names)', globals=globals(), number=1), 'seconds')

	stats = tracemalloc.take_snapshot().statistics('lineno')
	print(stats[0].size/1024, 'kb')

	data = run(file_names)

	####### Only return records after date.
	return_records_after = partial(return_records_after, date='1/1/2017')
	curr_records = filter(return_records_after, data)  # This is an iterator

	####### Return largest car makes for each gender


	# Remember we need to sort the data before we can group it since it needs to find the data consecutively.
	data.sort(key=lambda x: (x.gender, x.vehicle_make))

	grouped = groupby(data, key=lambda x: (x.gender, x.vehicle_make))

	car_dic = dict(Male={}, Female={})

	for key, groups in grouped:
		car_dic[key[0]] = {**car_dic[key[0]], **{key[1]: sum([1 for group in groups])}}

	for key, val in car_dic.items():
		vehicle_make = sorted(car_dic[key], reverse=True, key=lambda x: car_dic[key][x])[0]
		print(key, vehicle_make, car_dic[key][vehicle_make])
