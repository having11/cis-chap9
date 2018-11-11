# Type code for classes here
class ItemToPurchase(object):
    def __init__(self):
        self.item_name="none"
        self.item_price=0
        self.item_quantity=0
        self.item_description = "none"
    def print_item_cost(self):
        print("%s %d @ $%d = $%d"%(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))
    def get_total_cost(self):
        return int(self.item_price*self.item_quantity)
    def print_item_description(self):
        print("%s: %s"%(self.item_name,self.item_description))
		
class ShoppingCart():
	def __init__(self):
		self.customer_name = "none"
		self.current_date = "January 1, 2016"
		self.cart_items = []
	def print_name_date(self):
		print("%s's Shopping Cart - %s" % (self.customer_name, self.current_date))
	def add_item(self, ItemToPurchase):
		self.cart_items.append(ItemToPurchase)
	def remove_item(self, item_name):
		found = False
		for item in self.cart_items:
			if item.item_name == item_name:
				self.cart_items.remove(item)
				found = True
				print(self.cart_items)
				break
		if not found:
			print("Item not found in cart. Nothing removed")
	def modify_item(self, name, qty):
		found = False
		for item in self.cart_items:
			if item.item_name == name:
				ItemToPurchase = item
				if ItemToPurchase.item_price == 0 and ItemToPurchase.item_quantity == 0 and ItemToPurchase.name == "none" and ItemToPurchase.item_description == "none":
					#it's default
					pass
				else:
					item.item_quantity = qty
				found = True
				break
		if not found:
			print("Item not found in cart. Nothing modified.")
	def get_num_items_in_cart(self):
		return len(self.cart_items)
	def get_cost_of_cart(self):
		total = 0
		for item in self.cart_items:
			total += item.get_total_cost()
		return total
	def print_total(self):
		self.print_name_date()
		if self.get_num_items_in_cart() > 0:
			#print("Total: %i" % get_cost_of_cart)
			print("Number of Items: %d\n"%len(cart.cart_items))
			for item in self.cart_items:
				item.print_item_cost()
			print("\nTotal: %d" % self.get_cost_of_cart())
		else:
			print("SHOPPING CART IS EMPTY")
	def print_descriptions(self):
		self.print_name_date()
		print("\nItem Descriptions")
		for item in self.cart_items:
			item.print_item_description()
			
cart = ShoppingCart()

name = input("Enter customer's name:\n")
date = input("Enter today's date:\n\n")

cart.customer_name = name
cart.current_date = date

print("\nCustomer name: %s\nToday's date: %s" % (cart.customer_name,cart.current_date))
def print_menu():
	print("MENU")
	print("a - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items' descriptions\no - Output shopping cart\nq - Quit")

def output_shopping_cart():
	print("OUTPUT SHOPPING CART")
	cart.print_total()
def output_items_desc():
	print("OUPUT ITEMS' DESCRIPTIONS")
	cart.print_descriptions()
def add_item():
	print("ADD ITEM TO CART")
	name = input("Enter the item name:\n")
	description = input("Enter the item description:\n")
	price = int(input("Enter the item price:\n"))
	quantity = int(input("Enter the item quantity:\n"))
	new_item = ItemToPurchase()
	new_item.item_name = name
	new_item.item_price = price
	new_item.item_description = description
	new_item.item_quantity = quantity
	cart.add_item(new_item)
def remove_item():
	print("REMOVE ITEM FROM CART")
	name = input("Enter name of item to remove:\n")
	cart.remove_item(name)
def change_qty():
	print("CHANGE ITEM QUANTITY")
	item_name = input("Enter the item name:\n")
	item_qty = input("Enter the new quantity:\n")
	cart.modify_item(item_name, int(item_qty))
	
print_menu()
choice = input("Choose an option:\n")
while choice != 'q':
	#print(cart.cart_items)
	if choice == 'a':
		add_item()
	elif choice == 'r':
		remove_item()
	elif choice == 'c':
		change_qty()
	elif choice == 'i':
		output_items_desc()
	elif choice == 'o':
		output_shopping_cart()
	elif choice == 'q':
		break
	print_menu()
	choice = input("Choose an option:\n")
	
