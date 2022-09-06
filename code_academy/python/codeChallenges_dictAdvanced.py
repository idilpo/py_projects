"""
Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function
should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.
"""

def word_length_dictionary(words):
    d = {}
    for w in words:
        d[w] = len(w)
    return d

print(word_length_dictionary(["apple", "dog", "cat"]))
print(word_length_dictionary(["a", ""]))



"""
Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function 
should return a dictionary containing the frequency of each element in words.
"""

def frequency_dictionary(words):
    freqs = {}
    for w in words:
        if w not in freqs:
            freqs[w] = 0
        freqs[w] += 1
    return freqs

print(frequency_dictionary(["apple", "apple", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))



"""
Create a function named unique_values that takes a dictionary as a parameter. The function 
should return the number of unique values in the dictionary.
"""

def unique_values(d):
    unique_vals = d.values()
    unique_number = set(unique_vals)
    return len(unique_number)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
print(unique_values({0:3, 1:3, 4:3, 5:3}))



"""
Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary 
where the key is a last name and the value is a list of first names. For example, the dictionary might look like this: 
names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
The function should return a new dictionary where each key is the first letter of a last name, and the value is the number 
of people whose last name begins with that letter. So in example above, the function would return: {"S" : 4, "L": 3}
"""

def count_first_letter(names):
    letters = {}
    for k in names:
        first_letter = k[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[k])
    return letters

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
