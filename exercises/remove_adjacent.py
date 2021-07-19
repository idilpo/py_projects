# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

list_of_nums = [1, 2, 2, 3]
def remove_adjacent(nums):
    modified = list(set(list_of_nums))
    return modified
print(remove_adjacent(list_of_nums))


# tests:
# remove_adjacent([1, 2, 2, 3]) --> [1, 2, 3]
# remove_adjacent([2, 2, 3, 3, 3]) --> [2, 3]