# The printed output for the names list will look exactly like it did in the first line.
# During each iteration, the name variable is set to a string taken from the list.
# Then the assignment statement creates a new string (name.lower().replace(" ", "_")) and changes the name variable to that string.
# It doesn't modify the contents of the names list at all. To modify the list you must operate on the list itself, using range.

names = ["Joey Tribbiani", "Ross Geller", "Rachel Green", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for i in names: #range(len(usernames))
    usernames.append(i.lower().replace(" ", "_"))

print(usernames)
