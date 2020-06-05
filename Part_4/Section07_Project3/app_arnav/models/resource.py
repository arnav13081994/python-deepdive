'''
This is the base class, Resource

Functionality:

Properties:
	name : user-friendly name of resource instance (e.g.Intel Core i9-9900K)
	manufacturer - resource instance manufacturer (e.g. Nvidia)
	total : inventory total (how many are in the inventory pool)
	allocated : number allocated (how many are already in use)
	category - computed property that returns a lower case version of the class name

Methods:
	claim(n) : method to take n resources from the pool (as long as inventory is available)
	freeup(n) : method to return n resources to the pool (e.g. disassembled some builds)
	died(n) : method to return and permanently remove inventory from the pool (e.g. they broke something) - as long as total available allows it
	purchased(n) - method to add inventory to the pool (e.g. they purchased a new CPU)

Dunders:
	a __str__ representation that just returns the resource name
	a mode detailed __repr__ implementation

Helper Functions: Maybe put this in a seperate module if I am going to reuse across class instances like validators.py
'''


class Resource:


	def __init__(self, name, manufacturer, total, allocated):
		# TODO Add Validator code to make sure the instance attributes get set correctly.
		self._name = name
		self._manufacturer = manufacturer
		self._total = total # Current Total
		self._allocated = allocated # Current Allocated
		self.category = self.__class__.__name__.lower()

	@property
	def allocated(self):
		return self._allocated

	@property
	def total(self):
		return self._total

	@property
	def name(self):
		return self._name

	@property
	def manufacturer(self):
		return self._manufacturer

	@allocated.setter
	def allocated(self, value):
		# TODO Add Validator code to make sure the instance attributes get set correctly.
		self._allocated = value

	@total.setter
	def total(self, value):
		# TODO Add Validator code to make sure the instance attributes get set correctly.
		self._total = value


	def claim(self, n):
		''' Will take n resources from the pool (as long as inventory is available) '''
		# Check number of available resources in the pool. If sufficient then claim, and update it.
		if n <= (self.total - self.allocated):
			self.allocated += n
		raise ValueError("Can't claim more resources than currently available.")

	def freeup(self, n):
		''' Will return n resources to the pool (e.g. disassembled some builds) '''
		# Check number of available resources in the pool. If sufficient then claim, and update it.
		if n <= self.allocated:
			self.allocated -= n
		raise ValueError("Can't freeup more resources than currently allocated.")


	def died(self, n):
		'''Will return and permanently remove inventory from the pool (e.g. they broke something) - as
		 long as total available allows it'''

		if n <= self.total:
			self.total -= n
		raise ValueError("Can't kill more resources than available")


	def purchased(self, n):
		'''Will add inventory to the pool (e.g. they purchased a new CPU) '''
		self.total += n




	def __str__(self):
		return self.name

	def __repr__(self):
		kwargs = {k.strip('_'): v for k, v in vars(self).items()}
		return f'{self.category}({kwargs})'



if __name__ == "__main__":
	r1 = Resource("Intel Core i9-9900K", "Intel", 10, 0)
	print(r1)
	type(r1)

