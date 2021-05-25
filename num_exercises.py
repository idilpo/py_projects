# printing odd numbers below 50, in descending order:
num_list = []
for num in range(50, 0, -1):
    if (num % 2 != 0):
        num_list.append(num)
print(num_list)
print("\n")


# printing prime numbers between a range:
lower = int(input("Lower limit value for the range: "))
upper = int(input("Upper limit value for the range: "))
for number in range(lower, upper + 1):
   if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number, end=", ")



print("\n")
# printing max and min numbers in an inputted list by the user (using built-in functions):
user_input = []
n = int(input("Enter how many items you would like to input: "))
for i in range(0, n):
    print("Enter %d number:" % (i + 1))
    element = int(input())
    user_input.append(element)  # adding the element
print(user_input)
input_sorted = user_input.sort()
print(input_sorted)
largest = max(user_input)
smallest = min(user_input)
print("Largest element is: %d." % (largest))
print("Smallest element is: %d." % (smallest))


print("\n")
# printing max and min numbers in an inputted list by the user (using indexing):
user_input = []
n = int(input("Enter how many items you would like to input: "))
for i in range(0, n):
    print("Enter %d number:" % (i + 1))
    element = int(input())
    user_input.append(element)  # adding the element

print(user_input)
user_input.sort()
input_sorted = user_input
print("Largest element is: %d." % (input_sorted[-1]))
print("Smallest element is: %d." % (input_sorted[0]))


