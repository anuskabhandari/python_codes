## used to apply a function to all elements
#syntax: map(function ,iterable)

numbers=[1,2,3,4]

squared = list(map(lambda x: x**2 , numbers))

print(squared)