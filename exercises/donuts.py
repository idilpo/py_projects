# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

c = int(input("Input count: "))

def donuts(count):
  if count <= 10:
      return "Number of donuts: %d" %(count)
  else:
      return "Number of donuts: many"

print(donuts(c))