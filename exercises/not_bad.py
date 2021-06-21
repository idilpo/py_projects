# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
    n = s.find('not')
    b = s.find('bad')
    if b > n:
        s = s[:n] + 'good' + s[b + 3:]
    return s

# tests:
print(not_bad('This movie is not so bad')) # 'This movie is good'
print(not_bad('This dinner is not that bad!')) # 'This dinner is good!'
print(not_bad('This tea is not hot')) # 'This tea is not hot'
print(not_bad("It's bad yet not"))  # "It's bad yet not"