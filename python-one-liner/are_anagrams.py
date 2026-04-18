# Checking if they contain the same elements with same freaquency , but order can be different
list1 = ['a', 'b', 'c']
list2 = ['c', 'a', 'b']
are_anagrams = sorted(list1) == sorted(list2)
print(are_anagrams)