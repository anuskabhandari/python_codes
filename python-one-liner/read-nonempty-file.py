# REad a file and returns only non-empty lines
lines = [line.strip() for line in open('text.txt') if line.strip()]
print(lines)
# text.txt ma gap xaa words ma but output aauda gap aaudaina