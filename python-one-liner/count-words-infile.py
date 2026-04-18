# Count the number of words in file
word_count = sum(len(line.split()) for line in open("text.txt"))
print(word_count)