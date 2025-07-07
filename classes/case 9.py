# Case 9:-Simple Inventory System




class Product:
    def __init__(self, name, price, quantity ):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_info(self):
         if self.quantity ==0:
            print("enter the quantity ")
         else:
            print(f'{self.name},\n{self.price} price of product,\n{self.quantity} quantity ')

    def update_quantity(self,name, quantity):
        #   if name in self.name:
        if self.quantity > 0 and self.quantity< quantity:
            self.quantity = self.quantity + quantity
            return
        print(f"Out of stock, requested {abs(quantity)} available only {self.quantity} and short {abs(self.quantity-abs(quantity))}")
    
    def is_in_stock(self):
        return self.quantity > 0
           
#example 1
factory = Product("adidas", "2000",3)
factory.get_info()
factory.update_quantity("adidas", 6)
factory.update_quantity("adidas", 9)
factory.is_in_stock()