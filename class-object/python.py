class FoodOrder:
    def __init__(self, customer_name, price, item):
        self.customer_name = customer_name
        self.price = price
        self.item = item

    def show_order(self):
        print("Customer Name:", self.customer_name)
        print("Item:", self.item)
        print("Price:", self.price)


O1 = FoodOrder("Rekha", 100, "Milk")
O2 = FoodOrder("Sita", 200, "Bread")

O1.show_order()