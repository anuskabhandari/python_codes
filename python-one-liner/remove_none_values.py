# Removing the none values
lst = [1 , None , 2 , None , 3 , None , 4 , None ]
cleaned = [x for x in lst if x is not None]
print(cleaned)