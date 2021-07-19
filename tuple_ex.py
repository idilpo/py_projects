
# finding all the tuples for a particular number.
a = [(1, 2), (1, 4), (3, 5), (5, 7)]

# the first number to match:
sol1 = [item for item in a if item[0] == 1]
sol2 = [(x, y) for x, y in a if x == 1]

# searching for tuples with 1 in them:
sol3 = [item for item in a if 1 in item]



