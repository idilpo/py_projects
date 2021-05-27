# At a particular company, employees’ salaries are raised progressively, calculated using the following formula:
# salary = salary + salary x (raise percentage)
# Raises are predefined as given below, according to the current salary of the worker.
# if 0<salary<=1000 then 15%
# if 1000<salary<=2000 then 10%
# if 2000<salary<=3000 then 5%
# if 3000<salary then 2.5%
# Write a program that asks the user to enter their salary.
# Then your program should calculate and print the raised salary of the user.
# Some example program runs:
# Please enter your salary: 1000 Your raised salary is 1150.0.
# Please enter your salary: 2500 Your raised salary is 2625.0.

salary = float(input("Please enter your salary: "))
if (0 < salary <= 1000):
    salary += salary * 0.15
    print("Your raised salary will be: %.1f" % (salary))
elif (1000 < salary <= 2000):
    salary += salary * 0.10
    print("Your raised salary will be: %.1f" % (salary))
elif (2000 < salary <= 3000):
    salary += salary * 0.05
    print("Your raised salary will be: %.1f" % (salary))
elif (3000 < salary):
    salary += salary * 0.025
    print("Your raised salary will be: %.1f" % (salary))
else: # if salary is inputted less than 0,
    while (salary < 0):
        salary = float(input("Please enter a valid salary: "))

