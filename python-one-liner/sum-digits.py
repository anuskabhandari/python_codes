# The sum of the digits of a number
n = int(input("Enter a digits of a number: "))
digit_sum = sum(map(int , str(abs(n))))
print(digit_sum)