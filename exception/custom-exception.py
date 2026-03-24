#custom  exception
#user defined exception to handle the error and provide more usability and flexibilty

class InsufficientBalanceError(Exception):
    pass

def withdraw(amount,balance):
    if amount > balance:
        raise InsufficientBalanceError("  Not enough money")
withdraw = withdraw(100, 100987)
print(withdraw)