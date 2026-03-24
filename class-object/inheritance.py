class Ride:
    def __init__(self, user, distance):
        self.user = user
        self.distance = distance

    def fare(self):
        print(self.distance)
        print("This is for the calculation of fare")

## Inheritance
class BikeRide(Ride):
    def __init__(self, user, distance):
        super().__init__(user, distance)
    def fare(self):
        print("This is bike fare" , self.distance*50)

class CarRide(Ride):
    def __init__(self, user, distance):
        super().__init__(user, distance)
    def fare(self):
        print("This is car fare" , self.distance*100)

r1 = BikeRide("Bob", "10")
r1.fare()
r2 = BikeRide(" john", "20")
r2.fare()