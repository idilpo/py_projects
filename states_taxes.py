# Depending on where an individual is from we need to tax them appropriately.
# The states of CA, MN, and NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and the corresponding
# state to assure that they are taxed by the right amount.

state = input("Please enter your state: ")

if (state == "CA"):
    purchase_amount = int(input("Please enter the amount of purchase: "))
    tax_amount = .075
    total_cost = purchase_amount * (1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
    print(result)

elif (state == "MN"):
    purchase_amount = int(input("Please enter the amount of purchase: "))
    tax_amount = .095
    total_cost = purchase_amount * (1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
    print(result)

elif (state == "NY"):
    purchase_amount = int(input("Please enter the amount of purchase: "))
    tax_amount = .089
    total_cost = purchase_amount * (1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)
    print(result)

else:
    state = input("Please enter a valid state: ")
