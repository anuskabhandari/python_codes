class Ride:
    def __init__(self,user , distance):
        self.user = user
        self.__distance = distance
    def get_distance(self):
        return self.__distance
    def set_distance(self,distance):
        if distance > 0:
               self.__distance= distance  ## hiding the distance so that it cannot be changed
r = Ride("Anuska" ,5)
r.set_distance(10)

# get distance
print(r.get_distance())