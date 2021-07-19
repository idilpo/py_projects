# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

str_list = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']

def front_x(words):
    list_of_xs = []
    list_of_non_xs = []
    for i in words:
        if i[0] == 'x':
            list_of_xs.append(i)
        else:
            list_of_non_xs.append(i)

    return sorted(list_of_xs) + sorted(list_of_non_xs)

print(front_x(str_list))


# tests:
# front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) --> ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
# front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) --> ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
# front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) --> ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
