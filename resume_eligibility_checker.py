#Take the input of the user name
name=input("Enter your name:")
experience=int(input("Enter years of ecperince:"))
if experience>=5:
    print(name,"is eligible for the Senior Developer role")
else:
    print(name,"is eligible for Junior Developer role")