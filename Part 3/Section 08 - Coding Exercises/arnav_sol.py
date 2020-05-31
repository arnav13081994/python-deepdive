from datetime import date, datetime
from decimal import Decimal
from json import JSONEncoder, dumps, loads, JSONDecoder


class Stock:
	def __init__(self, symbol, date, open_, high, low, close, volume):
		self.symbol = symbol
		self.date = date
		self.open = open_
		self.high = high
		self.low = low
		self.close = close
		self.volume = volume

	def __repr__(self):
		return f'Stock(symbol={self.symbol}, date={self.date}, open={self.open}, high={self.high},' \
		       f' low={self.low}, close={self.close},  volume={self.volume})'

	def toJSON(self):
		"""
		This class method will return a dictionary that will let the deserializer know the objecttype as well
		"""
		return {
			'objecttype': 'Stock',
			'properties': {
				'symbol': self.symbol,
				'date': self.date,
				'open': self.open,
				'high': self.high,
				'low': self.low,
				'close': self.close,
				'volume': self.volume
			}
		}


class Trade:
	def __init__(self, symbol, timestamp, order, price, volume, commission):
		self.symbol = symbol
		self.timestamp = timestamp
		self.order = order
		self.price = price
		self.commission = commission
		self.volume = volume

	def __repr__(self):
		return f'Trade(symbol={self.symbol}, timestamp={self.timestamp}, order={self.order}, price={self.price},' \
		       f' commission={self.commission}, volume={self.volume})'

	def toJSON(self):
		"""
		This class method will return a dictionary that will let the deserializer know the objecttype as well
		"""
		return {
			'objecttype': 'Trade',
			'properties': {
				'symbol': self.symbol,
				'timestamp': self.timestamp,
				'order': self.order,
				'price': self.price,
				'commission': self.commission,
				'volume': self.volume
			}
		}


class CustomJSONEncoder(JSONEncoder):

	def __init__(self, *args, **kwargs):

		my_params = {
			"indent": 2,
		}

		# By default, overriding any arguements mentioned here regardless of what the dev puts to maintain consistency
		super().__init__(*args, **{**kwargs, **my_params})


	#  TODO In python 3.8 you can use singledispatchemthod which lets you decorate class instace methods

	def default(self, obj):
		''' The encoder will call this functoin when it emncounters something it doesn't know how to serialise.'''

		try:
			if isinstance(obj, Stock) or isinstance(obj, Trade):
				return obj.toJSON()
			elif isinstance(obj, Decimal):
				return f'Decimal({str(obj)})'
			elif isinstance(obj, date) or isinstance(obj, datetime):
				return obj.isoformat()

		#  Best to call the parents default so that correct error handling and reporting functionality can be tapped into.
		except TypeError:
			super().default(obj)



if __name__ == "__main__":
	activity = {
		"quotes": [
			Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('338.64'), Decimal('337.60'),
			      Decimal('338.19'),
			      365_607),
			Stock('AAPL', date(2018, 11, 22), Decimal('176.66'), Decimal('177.25'), Decimal('176.64'),
			      Decimal('176.78'),
			      3_699_184),
			Stock('MSFT', date(2018, 11, 22), Decimal('103.25'), Decimal('103.48'), Decimal('103.07'),
			      Decimal('103.11'),
			      4_493_689)
		],

		"trades": [
			Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
			Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
		]
	}

	dup_1 = dumps(activity, cls=CustomJSONEncoder, indent=10)
	print(dup_1)
