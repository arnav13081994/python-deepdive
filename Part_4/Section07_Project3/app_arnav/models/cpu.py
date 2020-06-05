from numbers import Integral
from Part_4.Section07_Project3.app_arnav.models.resource import Resource


class CPU(Resource):

	def __init__(self, name: str, manufacturer: str, total: int, allocated: int, cores: int,
	             socket: str, power_watts: int):
		# Calling super would automatically validate and initialise the instance
		super().__init__(name, manufacturer, total, allocated)

		# validations
		self.validate(socket, str, min_length=1)
		self.validate(cores, Integral, min_value=1)
		self.validate(power_watts, Integral, min_value=1)

		self._cores = cores
		self._socket = socket.strip()
		self._power_watts = power_watts

	@property
	def cores(self):
		return self._cores

	@property
	def socket(self):
		return self._socket

	@property
	def power_watts(self):
		return self._power_watts



if __name__ == "__main__":
	c1 = CPU("RYZEN Threadripper 2990WX", "AMD", 10, 3, 32, "sTR4", 250)
	type(c1)
	print(c1.category)
