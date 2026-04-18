# Generate a random password
import random , string
pwd = ''.join(random.choices(string.ascii_letters + string.digits , k =12) )
print(pwd)