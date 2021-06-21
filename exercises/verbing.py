# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

word = input("Input: ")

def verbing(s):
    if len(s) >= 3:
        if s[-3:] != 'ing':
            s = s + 'ing'
        else:
            s = s + 'ly'
    return s

print(verbing(word))