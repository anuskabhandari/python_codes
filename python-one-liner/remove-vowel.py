# Remove vowels from a string
s = input("Enter a string: ")
no_vowels = ''.join(c for c in s if c.lower() not in 'aeiou')
print(no_vowels)
