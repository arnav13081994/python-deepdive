from dis import dis

name = ['Guido']

class MyClass:
	name = 'Raymond Senior'
	list_1 = [name] * 3
	list_2 = [(name[:], id(name)) for __ in range(2)]
	list_3 = [(name, id(name)) for _ in range(2)]

	@classmethod
	def hello(cls):
		# global name
		print(name, id(name), name[:], id(name))
		name.append('mutated')
		print(name, id(name), name[:], id(name))
		return f'{name} says hello'

	@classmethod
	def f_3(cls):
		print("F3 Instance method running..........")
		l = []
		for i in range(2):
			l.append((name, id(name)))
		return l


	@classmethod
	def f_2(cls):
		print(" F2 Instance method running..........")
		l = []
		for i in range(2):
			l.append((name[:], id(name)))
		return l



#
# class SubClass(MyClass):
# 	pass


if __name__ == "__main__":
	# dis('print(5)')

	c = MyClass()
	# d = SubClass()
	# print(c.list_1)

	# dis('print(MyClass().list_2)')

	print(c.hello())
	print("List 2 running.....")
	print(c.list_2)
	print(c.f_2())
	print("List 3 running.....")
	print(c.list_3)
	print(c.f_3())

# print(d.list_2)
	# print(d.f())
	# print(c.hello())
	# print(type(c).__name__)


	# # d = SubClass()
	# print(d.list_1)
	# print(d.list_2)
	# print(d.hello())
	# print(type(d).__name__)
