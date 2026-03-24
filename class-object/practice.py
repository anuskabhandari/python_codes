class Restaurant :
    # class variable
    menu = {
        "Pizza": 500,
        "Bread": 200,
        "burger": 200,
        "pasta": 500
    }

    def __init__(self,customer_name):
        # object attributes
        self.customer_name = customer_name
        self.order = []
        self.order_summary = {}
        self.discount = 0

    def place_order(self ,item,quantity):
        if item in Restaurant.menu:
            price = Restaurant.menu[item] * quantity
            order = (item ,quantity , price)
            self.order.append(order)
            self.order_summary[item] = self.order_summary.get(item, 0) + quantity
            print(f"{self.customer_name} ordered {quantity} x {item}")
        else:
            print(f"Sorry, {item} is not available in the menu.")


    #Apply discount(percentage)

    def apply_discount(self,percent):
        self.discount = percent
        print(f"A discount of {percent}% has been applied for {self.customer_name}")


        ## Calculate TOtal bill

    def calculate_total(self):
        total_func = lambda order: order[2]  # Lambda function to get price
        total = sum(total_func(order) for order in self.order)  # Loop + sum
        if self.discount > 0:
            total = total - (total * self.discount / 100)  # Apply discount
        return total

    ## Unique items ordered using get
    def unique_items_ordered(self):
        return set(item[0] for item in self.order)

    def show_summary(self):
        print("\n------ Order Summary for", self.customer_name, "------")
        print("Item-wise quantity (dictionary):", self.order_summary)
        print("Unique items ordered (set):", self.unique_items_ordered())
        print("Discount applied:", self.discount, "%")
        print("Total bill after discount:", self.calculate_total(), "INR")
        print("--------------------------------------\n")


# object
c1 = Restaurant("Anuska")
c2 = Restaurant("Simran")
c1.place_order("Pizza", 3)
c1.apply_discount(10)

c2.place_order("Pasta", 2)
c2.apply_discount(5)
## show summaries
c1.show_summary()
c2.show_summary()



