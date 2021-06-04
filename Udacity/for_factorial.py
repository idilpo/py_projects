product = 1 # product is initialised to 1 in the beginning

try:
    number = int(input("Enter the number you'd like to calculate the factorial of: "))
except (ValueError):
    number = int(input("Please enter a valid input: "))

for i in range(2, number+1):
    product *= i
print("Factorial of %d is %d." % (number, product))