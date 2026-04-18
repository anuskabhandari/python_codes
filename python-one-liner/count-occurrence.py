# Count occurences of elements in a list
from collections import Counter
lst = [ 1, 2, 3 ,1 ,1, 1 , 6 ,7,3,2 , 7, 7,1]
counts = Counter(lst)
print(counts)