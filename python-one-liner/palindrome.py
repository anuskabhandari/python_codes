s = input("Enter a string: ")
is_palindrome = lambda s : s == s[::-1]
print(is_palindrome(s))