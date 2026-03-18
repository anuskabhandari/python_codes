check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(5))

##Lambda Returning Multiple Values
calc = lambda x: (x, x**2, x**3)

print(calc(3))

## Nested Lambda 
multiply = lambda x: lambda y: x * y

result = multiply(5)(3)
print(result)


