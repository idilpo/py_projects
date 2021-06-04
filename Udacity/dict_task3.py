fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for item, count in basket_items.items():
    if item in fruits:
       fruit_count += count
    else:
        not_fruit_count += count

print("The number of fruits is {}.\nThere are {} objects that are not fruits.".format(fruit_count, not_fruit_count))