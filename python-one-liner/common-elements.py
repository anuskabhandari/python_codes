# Finding common elements in 3 lists
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2,3 , 4,]
c = [3,4]

common = set(a) & set(b) & set(c)
print(common)
