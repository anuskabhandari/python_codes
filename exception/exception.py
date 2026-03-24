#exception handling in python
#sytax error -wrong code
#runtime error - during program executon
#basic try except
#only test during development not  production
#during production the value must be analysed at initial point

try:
    print('Inside try except block')
    num = int(input('Enter a number: '))
    print(10/num)
except ValueError:
    print('Invalid input.Please enter a number.')
except ZeroDivisionError:
    print('you cannot divide by zero')
