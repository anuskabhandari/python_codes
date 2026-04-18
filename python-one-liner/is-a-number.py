#Check if the string is a number
s = input("Enter a sth: ")
is_num = lambda s: s.replace('.', '',1).isdigit()
print(is_num(s))