# Case 7:- Restaurant Menu and Orders


class Restaurant:
    def __init__(self):
        self.menu = {}
        self.order = []

    def add_menu_item(self, name, price):
        if name in self.menu:
            print(f"{name} is already exixts")
            return
        self.menu.update({name: price})

    def print_menu(self):
        print(self.menu)

    def take_order(self, name, quantity):
        # Handle empty quantity
        menu = self.menu[name]
        print(menu)
        # CASE 1: lookup menu name from menu and validate
        # CASE 2: Get price of the menu
        # CASE 3: Update existing order entry by increasing the quantity
        order_amount = quantity * 40
        self.order.append({"name": name, "amount": order_amount, "quantity": quantity})

    def print_order(self):
        print(self.order)


# Exampel 1:
restaurant = Restaurant()
restaurant.add_menu_item("Chicken", 99)
restaurant.add_menu_item("Leg piece", 100)
# restaurant.print_menu()
restaurant.take_order("Chicken", 2)
# restaurant.take_order("lEG PIECE", 4)
# restaurant.take_order("Cheicken", 1)
restaurant.print_order()
