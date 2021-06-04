letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))


print(list(zip(['a', 'b', 'c'], [1, 2, 3])))


# unzip:
some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)
print(some_list)


