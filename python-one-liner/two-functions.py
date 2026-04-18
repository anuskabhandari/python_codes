# Compose two functions
compose = lambda f, g: lambda x: f(g(x))

f = lambda x: x * x      # square function
g = lambda x: x + 2      # add 2 function

x = 5

print(compose(f, g)(x))

"""
first ma g function execute vayo and 5+2= 7 vayo then
f function execute huda 7 ko vayera output 49 aayo
"""