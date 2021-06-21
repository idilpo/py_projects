# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.

sth = input("Input s: ")

def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        str_list = list(s)
        return "" + str_list[0] + str_list[1] + str_list[-1] + str_list[-2]

print(both_ends(sth))