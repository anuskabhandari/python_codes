# Counting vowels in the string
s = input("Enter a string: ")
count = sum(c in 'aeiouAEIOU' for c in s)
print(count)