# Flatten nested lists (any depth using recursion)
flatten = lambda l: sum(map(flatten, l), []) if isinstance(l, list) else [l]

data = [1, [2, [3, 4], 5], 6]

print(flatten(data))
