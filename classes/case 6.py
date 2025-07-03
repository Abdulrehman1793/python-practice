# Case 6:- Restaurant Menu and Orders
class Restaurant:
    def __init__(self):
        self.menu = {}
        self.order = []

    def add_menu_item(self, name, price):
        if name in self.menu:
            print(f"{name} is already exits")
            return
        self.menu.update({name: price})

    def print_menu(self):
        print(self.menu)

    def take_order(self, name, quantity):
        # Handle empty quantity
        if quantity <= 0:
            print(f'{name},quantity should be greater than 0')
            return
        
        # CASE 1: lookup menu name from menu and validate
        if name not in self.menu:
            print(f'{name} "is not available in menu"')
            return
        else:
            price = self.menu[name]
            print(f'{name} {price},its is available  ')
            order_amount = quantity * price
        self.order.append({"name": name, "amount": order_amount, "quantity": quantity})
        print(self.order)

        # CASE 2: Get price of the menu
    def get_price(self, name, quantity ):
        price =  quantity * self.menu[name]

    def print_order(self):
        print(self.order)
    
    def display(self):
         print(f'{self.menu}, "order_amount"')


#exampel 1

restaurant = Restaurant()
restaurant.add_menu_item("chicken", 85 )
restaurant.add_menu_item("lollipop", 120)
restaurant.add_menu_item("chicken", 85)
restaurant.print_menu()
restaurant.take_order("chicken", 2)
restaurant.take_order("lollipop", 0)
restaurant.get_price("chicken" , 2)
restaurant.get_price("lollipop", 0)
restaurant.print_order()

#example 2 

khalid = Restaurant()
khalid.add_menu_item("rice", 120)
khalid.add_menu_item("desert", 60)
khalid.print_menu()
khalid.take_order("rice", 2)
khalid.take_order("desert",4)
khalid.get_price("rice", 2)
khalid.get_price("desert",4)
khalid.print_order()


