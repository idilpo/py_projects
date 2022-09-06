"""
Define the function to accept one parameter — the word whose letters we are counting
Create a counter to keep track of unique letters
Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
Return the count after looping through all letters.
"""

def count_letters(word):
    counter = 0
    for letter in word:
        counter += 1
    return counter

print(count_letters(""))
print(count_letters("alphabet"))



"""
Write a function called unique_english_letters that takes the string word as a parameter. The function should return 
the total number of unique letters in the string. Uppercase and lowercase letters should be counted as different letters.
"""

def unique_english_letters(string):
    unique_letter_list = []
    for letter in string:
        if letter not in unique_letter_list:
            unique_letter_list.append(letter)
    return len(unique_letter_list)

print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))



"""
Count the number of occurrences of a certain letter within a string. Our function will accept a parameter for a string and 
another for the character which we are going to count. These are the steps we need to take:

Define the function to accept two parameters. word for the input string and x for the single character
Create a counter to keep track of the occurrences
Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
Return the counter after looping through the entire string.
"""

def numberOfLetters(word, char):
    c = 0
    for letter in word:
        if letter == char:
            c += 1
    return c

print(numberOfLetters("mississippi", "s"))
print(numberOfLetters("Apple", "p"))
print(numberOfLetters("mississippi", "m"))



"""
Compare against an entire string instead of a single character. This function should accept a string and a substring to compare against. 
The number of occurrences of the second parameter within the first parameter string are returned. What this means is that we are checking 
the number of occurrences of the shorter string (second parameter) within the longer string (first parameter). One way to accomplish this is 
using the split function.

Define the function to accept two parameters. word for the input string and x for the second string we are searching for
Split the string into substrings based on the second input parameter
Count the number of instances the substring appeared in the first input string based on the split string
Return the result
"""

def count_multi_char_x(str, sub_str):
    split = str.split(sub_str)
    print(split)
    return len(split)-1

print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))



"""
A function that is able to extract a portion of a string between two characters. The function will take three parameters where the first parameter 
is the string we are going to extract the substring from, the second input is the starting character of our substring and the third character is the 
ending character of our substring. 

Define the function to accept three parameters, one string and two characters
find the starting index of our substring using the second input parameter
find the ending index of our substring using the third input parameter
If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the 
starting and ending index)
If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case.
"""

def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return(word[start_ind+1:end_ind])
    return word

print(substring_between_letters("apple", "p", "e"))

"""
def substring_between(string, start_char, end_char):
    for ele in string:
        if ele == start_char:
            for item in string[ele+1:]:
                if item == end_char:
                    return string[start_char:end_char+1]

print(substring_between("apple", "p", "e"))
"""



"""
A function that is able to accept two inputs: one for a sentence and another for a number. The function returns True if every single 
word in the sentence has a length greater than or equal to the number provided. 

Define the function to accept two parameters, one string, and one number
Split up the sentence into an array of words
Loop through the words. If the length of any of the words is less than the provided number return False
If we made it through the loop without returning False then return True
"""

def x_length_words(sentence, number):
    words = sentence.split(" ")
    for w in words:
        if len(w) >= number:
            return True
        else: return False

print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))