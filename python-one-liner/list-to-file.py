lst = [1 , 2, 3, 4,5]
open('out.txt', 'w').write('\n'.join(map(str, lst)))
"""
1. map(str, lst)

 Converts all elements to string
(because file can only write strings)

2. '\n'.join(...)

 Joins elements with new line

3. write(...)

 Writes final string into out.txt
 """