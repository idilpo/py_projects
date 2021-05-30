# Create two lists. The first list should consist of odd numbers. The second list is should consist of even numbers.
# Merge these two lists. Multiply all values in the new list by 2.
# Use a loop to print the data type of the all values in the new list.

# Comment on the exercise: for the sake of an implementable answer, here the instruction "number" is considered as "digits".
odd_digits = [1, 3, 5, 7, 9]
even_digits = [0, 2, 4, 6, 8]
merged_list = odd_digits + even_digits # two lists are merged together using the built-in function "merge"
merged_list.sort() # the merged list is sorted in an increasing order with the buil-in function "sort"
for i in merged_list: # looping through the elements in the list, multiplying each by 2
    merged_list[i] *= 2
    print("Element in index[%d]: %d" % (i, merged_list[i]))
print("Updated list: {}" .format(merged_list))
