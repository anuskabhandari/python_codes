## used to filter elements based on conditions.

#syntax
#filter(function , iterable)

numbers =[1,2,3,4,5,6]

even_numbers =list(filter(lambda x: x%2==0 , numbers))
print(even_numbers)

## without lambda
def is_even(x):
    return x% 2==0
print(list(filter(is_even, numbers)))