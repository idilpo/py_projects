# You would like to count the number of fruits in your basket.
# In order to do this, you have the following dictionary and list of fruits.
# Use the dictionary and list to count the total number of fruits, but you
# do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for key, count in basket_items.items():
    if key in fruits:
        result += count

print("There are {} fruits in the basket.".format(result))