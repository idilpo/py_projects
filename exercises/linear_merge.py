# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

l1 = ['aa', 'xx', 'zz']
l2 = ['bb', 'cc']

def linear_merge(list1, list2):
    # the sorted function's time complexity = O(nlogn)
    # so, modified = sorted(list1 + list2) --> woudlnt work

    result = []
    while len(list1) and len(list2): # look at the two lists so long as both are non-empty.
        # take whichever element [0] is smaller:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))

    # tack on what's left:
    result.extend(list1)
    result.extend(list2)
    return result

print(linear_merge(l1, l2))

# tests:
# linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']) --> ['aa', 'bb', 'cc', 'xx', 'zz']
# linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']) --> ['aa', 'bb', 'cc', 'xx', 'zz']
# linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']) --> ['aa', 'aa', 'aa', 'bb', 'bb']
