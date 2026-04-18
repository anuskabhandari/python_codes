# SWap two variables in one liner
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Before swapping")
print("a =" , a)
print("b =" , b)
# one liner swap
a,b = b,a
print("After swapping")
print("a =" , a)
print("b =" , b)