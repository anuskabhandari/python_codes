#raising exception
#user defined exception to handle the error and provide more usability and flexibilty
def withdraw(balance,amount):
    if amount > balance:
        raise Exception("Not enough funds or insufficient balance")
    return balance-amount

withdraw =withdraw(100,1000)
print(withdraw)