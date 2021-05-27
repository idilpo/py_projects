# FIBONACCI using start and stop values inputted from the user.
sum = 0
start_val = int(input("Please enter the minimum values you would like the range to start from: "))

while (start_val < 0):
    start_val = int(input("Please enter a valid start value: "))

if (start_val >= 0):
    stop_val = int(input("Please enter the maximum values you would like the range to stop at: "))

    while (stop_val < start_val):
        stop_val = int(input("Please enter a valid stop value: "))
    else:
        for i in range(start_val, stop_val):
            sum += i
            print(i)
print("The sum of all numbers between the range(%d, %d) is %d." % (start_val, stop_val, sum))