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
			'objecttype': 'stock',
			'properties': {
				'symbol': {
					'objecttype': 'string',
					'value': self.symbol,
				},
				'date': {
					'objecttype': 'date',
					'value': self.date,
				},
				'open_': {
					'objecttype': 'decimal',
					'value': self.open,
				},
				'high': {
					'objecttype': 'decimal',
					'value': self.high,
				},
				'low': {
					'objecttype': 'decimal',
					'value': self.low,
				},
				'close': {
					'objecttype': 'decimal',
					'value': self.close,
				},
				'volume': {
					'objecttype': 'integer',
					'value': self.volume,
				},
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
			'objecttype': 'trade',
			'properties': {
				'symbol': {
					'objecttype': 'string',
					'value': self.symbol,
				},
				'timestamp': {
					'objecttype': 'datetime',
					'value': self.timestamp,
				},
				'order': {
					'objecttype': 'string',
					'value': self.order,
				},
				'price': {
					'objecttype': 'decimal',
					'value': self.price,
				},
				'commission': {
					'objecttype': 'decimal',
					'value': self.commission,
				},
				'volume': {
					'objecttype': 'integer',
					'value': self.volume,
				},
			}
		}


class CustomJSONEncoder(JSONEncoder):

	def __init__(self, *args, **kwargs):

		my_params = {
			"indent": 2,
		}

		# By default, overriding any arguments mentioned here regardless of what the dev puts to maintain consistency
		super().__init__(**{**kwargs, **my_params})

	#  TODO In python 3.8 you can use singledispatchemthod which lets you decorate class instace methods

	def default(self, obj):
		''' The encoder will call this function when it emcounters something it doesn't know how to serialise.'''
		try:
			if isinstance(obj, Stock) or isinstance(obj, Trade):
				return obj.toJSON()
			elif isinstance(obj, Decimal):
				return float(obj)
			elif isinstance(obj, date) or isinstance(obj, datetime):
				return obj.isoformat()
		#  Best to call the parents default so that correct error handling and reporting functionality can be tapped into.
		except TypeError:
			super().default(obj)


class CustomJSONDecoder(JSONDecoder):

	def __init__(self, *args, **kwargs):
		my_params = {
			"object_hook": self.deal_with_obj_hook,
			'parse_float': self.deal_with_parse_float,
		}

		# By default, overriding any arguments mentioned here regardless of what the dev puts to maintain consistency
		super().__init__(**{**kwargs, **my_params})


	def deal_with_parse_float(self, obj):
		return Decimal(obj)


	def deal_with_obj_hook(self, obj):
		''' This function will get all the dict objects root or nested and will need to return a dict object'''

		for key, value in obj.items():

			if key == 'objecttype':
				if value == 'decimal' or value == 'integer' or value == 'string':
					return obj['value']
				elif value == 'date':
					return date.fromisoformat(obj['value'])
				elif value == 'datetime':
					return datetime.fromisoformat(obj['value'])

			elif key == 'properties':

				cls_name = obj['objecttype']
				if cls_name == 'stock':
					return Stock(**obj['properties'])
				elif cls_name == 'trade':
					return Trade(**obj['properties'])


		else:
			return obj



if __name__ == "__main__":
	activity = {
		"quotes": [
			Stock('TSLA', date(2018, 11, 22), Decimal('338.19'), Decimal('338.64'), Decimal('337.60'),
			      Decimal('338.19'), 365_607),
			Stock('AAPL', date(2018, 11, 22), Decimal('176.66'), Decimal('177.25'), Decimal('176.64'),
			      Decimal('176.78'), 3_699_184),
			Stock('MSFT', date(2018, 11, 22), Decimal('103.25'), Decimal('103.48'), Decimal('103.07'),
			      Decimal('103.11'), 4_493_689)
		],

		"trades": [
			Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
			Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
		]
	}

	serialise = dumps(activity, cls=CustomJSONEncoder, indent=10)
	deserialise = loads(serialise, cls=CustomJSONDecoder)

	for k, v in deserialise.items():
		print(k, v)
