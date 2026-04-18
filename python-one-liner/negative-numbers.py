#Filter out negative and positive numbers
lst =[-1 , 2 , -2 ,3 ,-3, 4 ,-4, 5, 6, 7, 8]
positives = list(filter(lambda x: x>0, lst))
print(positives)
negatives = list(filter(lambda x: x<0, lst))
print(negatives)