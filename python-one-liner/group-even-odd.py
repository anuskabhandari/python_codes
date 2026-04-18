# Group  list by even and odd
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
groups = {'even': [x for x in lst if x % 2 == 0], 'odd': [x for x in lst if x % 2 != 0]}
print(groups)