# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

string1 = input("Input-1: ")
string2 = input("Input-2: ")

def front_back(a, b):
    a_middle = len(a) // 2
    b_middle = len(b) // 2
    if len(a) % 2 != 0:
        a_middle += 1
    if len(b) % 2 != 0:
        b_middle += 1
    return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]

print(front_back(string1, string2))


# tests:
# front_back('abcd', 'xy') --> 'abxcdy'
# front_back('abcde', 'xyz') --> 'abcxydez'
# front_back('Kitten', 'Donut') --> 'KitDontenut'

