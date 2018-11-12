#Part One
class CellPhone():
	def __init__(self, manu, modelnum, price):
		self.manufact = manu
		self.model = modelnum
		self.retail_price = price
	def set_manufact(self,manu):
		self.manufact = manu
	def set_model(self, model):
		self.model = model
	def set_retail_price(self, price):
		self.retail_price = price
	def get_manufact(self):
		return self.manufact
	def get_model(self):
		return self.model
	def get_retail_price(self):
		return self.retail_price

manu = input("Enter the manufacturer: ")
modelnum = input("Enter the model number: ")
price = float(input("Enter the retail price: "))
		
phone = CellPhone(manu,modelnum,price)
print("Here is the data that you entered:\nManufacturer: %s\nModel Number: %s\nRetail Price: $%f" % (phone.get_manufact(),phone.get_model(),phone.get_retail_price()))

#Part 2
class Employee():
	def __init__(self, name, ID, department, title):
		self.name = name
		self.ID = ID
		self.department = department
		self.title = title
	def display_data(self):
		print("Name: %s, ID Number: %s, Department: %s, Job Title: %s" % (self.name,self.ID,self.department,self.title))

employee_1 = Employee("Susan Meyers","47899","Accouting","Vice President")
employee_2 = Employee("Mark Jones","39119","IT","Programmer")
employee_3 = Employee("Joy Rogers","81774","Manufacturing","Engineer")

employee_1.display_data()
employee_2.display_data()
employee_3.display_data()
