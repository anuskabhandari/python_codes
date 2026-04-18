# Finding out the duplicate element from the list
lst = [1,2,3,4,5,6,7,8,9, 1]
duplicates = list(set([x for x in lst if lst.count(x)>1]))
print(duplicates)