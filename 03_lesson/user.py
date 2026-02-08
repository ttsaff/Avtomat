class User:

	def __init__(self, first_name, last_name):
	
		self.fname = first_name
		self.lname = last_name

	def sayLName(self):
		print("Моя фамилия ", self.lname)

	def sayFName(self):
		print("Меня зовут ", self.fname)
	
	def sayName(self):
		print("Полное имя ", self.fname, self.lname)