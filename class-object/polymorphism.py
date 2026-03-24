## same function works with diffrent types
class Animal:
    def speak(self):
        print("some sound")

class Dog(Animal):
    def speak(self):
        print("a dog")

class Cat(Animal):
    def speak(self):
        print("a cat")

# Objects
a = Animal()
d = Dog()
c = Cat()

# Same method name, different behavior
a.speak()
d.speak()
c.speak()