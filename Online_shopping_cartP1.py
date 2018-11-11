# Type code for classes here
class ItemToPurchase(object):
    def __init__(self):
        self.item_name="none"
        self.item_price=0
        self.item_quantity=0
    def print_item_cost(self):
        print("%s %d @ $%d = $%d"%(self.item_name,self.item_quantity,self.item_price,self.item_price*self.item_quantity))
    def get_total_cost(self):
        return int(self.item_price*self.item_quantity)

if __name__ == "__main__":
    # Type main section of code here
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    print("Item 1")
    item1.item_name = input('Enter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    print("\nItem 2")
    item2.item_name = input('Enter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    print('\nTOTAL COST')
    item1.print_item_cost()
    item2.print_item_cost()
    print('\nTotal: $%d' % int(item1.get_total_cost()+item2.get_total_cost()))
    
