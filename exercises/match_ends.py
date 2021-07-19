# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

str_list = ['aaa', 'be', 'abc', 'hello']

def match_ends(words):
    count = 0
    for i in words:
        if len(i) >= 2 and (i[0] == i[-1]):
            count += 1
    return count

print(match_ends(str_list))


# tests:
# match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) --> 3
# match_ends(['', 'x', 'xy', 'xyx', 'xx']) --> 2
# match_ends(['aaa', 'be', 'abc', 'hello']) --> 1