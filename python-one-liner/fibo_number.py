n = int(input("How many fibo numbers do you want to print? "))

fib = lambda n: (lambda f: [f.append(f[-1]+f[-2]) or f for _ in range(n-2)] and f)([0,1])[:n]

print(fib(n))