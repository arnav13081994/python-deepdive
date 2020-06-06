from numbers import Integral
from Part_4.Section07_Project3.app_arnav.models.resource import Resource


class Storage(Resource):

	def __init__(self, name: str, manufacturer: str, total: int, allocated: int, capacity_GB: int):
		# Calling super would automatically validate and initialise the instance
		super().__init__(name, manufacturer, total, allocated)

		# validations
		self.validate(capacity_GB, Integral, min_value=1)
		self._capacity_GB = capacity_GB

	@property
	def capacity_GB(self):
		return self._capacity_GB


if __name__ == "__main__":
	s1 = Storage("Thumbdrive", "Sandisk", 10, 3, 512)
	type(s1)
	print(s1.category)
	s1.capacity_GB = 256
