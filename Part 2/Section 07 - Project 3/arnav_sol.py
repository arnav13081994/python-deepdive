from collections import namedtuple
import datetime


def cast_data(row, headers):
	""" Given a row and a list of headers, it will convert every value to the right type and return the row"""

	converted_row = []
	for data, head in zip(row, headers):
		if head == 'Summons_Number' or head == "Violation_Code":
			data = int(data) or 'N/A'

		elif head == 'Issue_Date':
			(m, d, y) = data.split('/')
			data = datetime.datetime(int(y), int(m), int(d))

		else:
			data = str(data) or 'N/A'

		converted_row.append(data)

	yield converted_row


data = []
with open("nyc_parking_tickets_extract.csv") as f:
	headers = next(f).replace(" ", "_").strip("\n").split(',')  # an array of headers
	parking = namedtuple("Parking", headers)

	for row in f:
		data.append(parking(next(cast_data(row, headers))))

	print(data)
