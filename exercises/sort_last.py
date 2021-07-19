# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.

list_of_tuples = [(1, 3), (3, 2), (2, 1)]

def sort_last(tuples):
    sorted(tuples)
    return tuples[::-1]

print(sort_last(list_of_tuples))


# tests:
# sort_last([(1, 3), (3, 2), (2, 1)]) --> [(2, 1), (3, 2), (1, 3)]
# sort_last([(2, 3), (1, 2), (3, 1)]) --> [(3, 1), (1, 2), (2, 3)]
# sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]) --> [(2, 2), (1, 3), (3, 4, 5), (1, 7)]