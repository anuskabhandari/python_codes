# Capitalize the first letter of each word
s = input("Enter a string: ")
capitalized = ' '.join(word.capitalize() for word in s.split())
print(capitalized)