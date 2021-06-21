# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

word = input("Input: ")

def fix_start(s):
  first_char = s[0]
  rest = s[1:]
  fixed = rest.replace(first_char, "*")
  return first_char + fixed

print(fix_start(word))