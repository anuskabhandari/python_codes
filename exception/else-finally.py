#else and finally
#what is finaly
#what is try and except
#how else is used in exception handling

try:
    x=10/2
except ZeroDivisionError:
    print("you cannot divide by zero")
else:
    print("Success!",x)
finally:
    print("This always runs and works")
