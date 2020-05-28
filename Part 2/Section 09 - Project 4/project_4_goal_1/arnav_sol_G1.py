import csv
import os
from collections import namedtuple
import datetime
import tracemalloc
from timeit import timeit

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
	# stats = tracemalloc.take_snapshot().statistics('lineno')
	# print(stats[0].size / 1024, 'kb')

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


def run(file_names):
	for f_name in file_names:
		next(file_iter(f_name))

if __name__ == "__main__":
	tracemalloc.start()
	print(timeit('run(file_names)', globals=globals(), number=10), 'seconds')

	stats = tracemalloc.take_snapshot().statistics('lineno')
	print(stats[0].size/1024, 'kb')
