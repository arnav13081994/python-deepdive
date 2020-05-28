import csv
import datetime
import os
from collections import namedtuple

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


if __name__ == "__main__":
	data_dic = {}
	data = []
	for file_name in file_names:
		next(file_iter(file_name))

	for val in data_dic.values():
		tup = namedtuple('Tup', list(val.keys()))
		break

	for ssn, row in data_dic.items():
		data.append(tup(**row))

	for ind, dat in enumerate(data):
		print(f"row:{ind+1}, {dat}")



