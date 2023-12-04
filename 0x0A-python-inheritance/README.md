Python is able to allow subclasses inherit properties from parent classes.

Suppose we have a class Employee

class Employee:
	def __init__(self, firstName, lastName):
		self.firstName = firstName
		self.lastName = lastName

We can inherit properties of Employee using the following line of code:

class Manager(Employee):
	def __init__(self):
		pass
