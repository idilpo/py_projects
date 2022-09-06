"""
Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
The function should return the sum of the values of the dictionary.
"""

def sum_values(d):
    total = 0
    for v in d.values():
        total += v
    return total

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))



"""
Create a function named values_that_are_keys that takes a dictionary as a parameter. This 
function should return a list of all values in the dictionary that are also keys.
"""

def values_that_are_keys(dict):
    value_keys = []
    for v in dict.values():
        if v in dict:
            value_keys.append(v)
    return value_keys

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))



"""
Write a function named max_key that takes a dictionary as a parameter. The function should return the 
key associated with the largest value in the dictionary.
"""

def max_key(d):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for k, v in d.items():
        if v > largest_value:
            largest_value = v
            largest_key = k
    return largest_key




