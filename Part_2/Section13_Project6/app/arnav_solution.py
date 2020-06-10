import csv
'''

file --> data_parser --> filter 1 --> filter 2 --> ..... --> print_data

'''

def coroutine(gn):
	'''Decorator to prime the coroutine'''
	def inner(*args, **kwargs):
		g = gn(*args, **kwargs)
		next(g)
		return g
	return inner



@coroutine
def data_parser(fname):
	''' Opens the fname and parses it using the csv reader iterators and then passes the data to another generator'''
	yield
	with open(fname) as f:
		next(f) # Skip Headers
		csv_reader = csv.reader(f)
		for row in csv_reader:
			filter_data.send(row)


@coroutine
def print_data():
	while True:
		received = yield
		print(received)



@coroutine
def filter_data(next_gen, *filter_words):
	while True:
		row = yield
		for filter_word in filter_words:
			if filter_word not in row[0]:
				break
		else:
			next_gen.send(row)




if __name__ == "__main__":

	# set up the row printer
	print_data = print_data()

	# Set up the filters
	filter_data = filter_data(print_data, 'Chevrolet', 'Carlo', 'Landau')

	data = data_parser(
		'/Users/arnavchoudhury/Desktop/Coding/Python/python-deepdive/Part_2/Section13_Project6/app/cars.csv'
	)

	# Parse and Read the data
	for _ in data:
		pass
