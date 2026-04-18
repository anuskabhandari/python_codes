# Check if number is prime
n = int(input("Enter a number: "))
is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
print(is_prime(n))