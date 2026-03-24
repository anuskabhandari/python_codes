def login(username,password):
    if username != "admin":
        raise ValueError("User not found")
    if password != "1234":
        raise ValueError("Wrong Password ")
    return "Into login "
try:
    print(login("admin","1234"))

except ValueError as e:
    print(e)
