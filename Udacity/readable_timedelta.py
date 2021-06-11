# Write a function named readable_timedelta. The function should take one argument,
# an integer days, and return a string that says how many weeks and days that is.
# For example, calling the function and printing the result like this:
# print(readable_timedelta(10))
# should output the following:
# 1 week(s) and 3 day(s).

def readable_timedelta(days):
    return "%d week(s) and %d day(s)." % (days // 7, days % 7)

# test:
print(readable_timedelta(10))