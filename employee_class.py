class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

# p1 = Employee("Azian", "Khan", 5000)
# print(p1.first)
# print(p1.__repr__())
