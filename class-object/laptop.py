class Laptop:
    def __init__(self,brand , price):
        self.brand = brand
        self.price = price


    def show_details(self):
        print(self.brand)
        print(self.price)


# Creating object
L1 = Laptop("laptop",100)
#CALLING OBJECT
L1.show_details()
