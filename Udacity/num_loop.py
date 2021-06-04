# You need to write a loop that takes the numbers in a given list named num_list:
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together.
# If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.

odd_count = 0
sum_odds = 0
length = len(num_list)
i = 0
while (odd_count < 5) and (i < length):
    if (num_list[i] % 2 != 0):
        sum_odds += num_list[i]
        odd_count += 1
    i += 1

print ("The number of odd numbers added are: {}".format(odd_count))
print ("The sum of the odd numbers added is: {}".format(sum_odds))
