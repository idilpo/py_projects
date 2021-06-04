product = 1 # product is initialised to 1 in the beginning
current = 1 # tracks the current number

try:
    number = int(input("Enter the number you'd like to calculate the factorial of: "))
except (ValueError):
    number = int(input("Please enter a valid input: "))

while (current <= number):
    product *= current
    current += 1  # increment current with each iteration until it reaches number
print("Factorial of %d is %d." % (number, product))