# Create a program will compute the tax and the tip for a meal ordered at a restaurant.
# You can compute the tax as 8 percent of the meal amount and the tip as 10 percent of the meal amount
# (without the tax). The output from your program should include the tax amount, the tip amount, and
# the grand total for the meal including both the tax and the tip.
# a)Define the cost of the meal in the beginning of your program.
# Some several example program runs:
# Cost of the meal is 25 Eur.
# Sample Run: The tax is 2.00 Eur and the tip is 2.50 Eur, making the total 29.50 Eur. Cost of the meal is 68 Eur.
# Sample Run: The tax is 5.44 Eur and the tip is 6.80000000000001 Eur, making the total 80.24 Eur.
# b)Input the cost of the meal from the user.
# Some several example program runs:
# Please enter the cost of your meal: 100
# Sample Run: The tax is 8.00 Eur and the tip is 10.00 Eur, making the total 118.00 Eur.
# Please enter the cost of your meal: 68
# Sample Run: The tax is 5.44 Eur and the tip is 6.80 Eur, making the total 80.24 Eur.

meal = float(input("Please enter the cost of your meal: "))
if meal < 0:
    meal = float(input("Please enter a valid meal cost: "))
tax = meal * 0.08
tip = meal * 0.10
cost = meal + tax + tip
print("Tax: %.2f \nTip: %.2f\nTotal cost: %.2f" % (tax, tip, cost))
