"""
You are creating an app that allows users to interact and share their coding project ideas online. The first step is to provide your name
in the application and a greeting for other people to see which contains your name. Let’s create a function that is able to check if a user’s
name is located within their greeting. We need a function that accepts two parameters, a string for our sentence and a string for a name. The
function should return True if the name exists within the string (ignoring any differences in capitalization).

Define the function to accept two parameters, one string for the sentence and one string for the name
Convert all of the strings to the same case so we don’t have to worry about differences in capitalization
Check if the name is within the sentence. If so, then return True. Otherwise, return False
"""

def func(sentence, name):
    sentence = sentence.lower()
    name = name.lower()
    words = sentence.split(" ")
    if name in words:
        return True
    else: return False

def check_for_name(sentence, name):
  return name.lower() in sentence.lower()

print(func("My name is Jamie", "Jamie"))
print(func("My name is jamie", "Jamie"))
print(func("My name is JAMIE", "Jamie"))
print(func("My name is Samantha", "Jamie"))



"""
Create a function that extracts every other letter from a string and returns the resulting string.

Define the function to accept one parameter for the string
Create a new empty string to hold every other letter from the input string
Loop through the input string while incrementing by two every time
Inside the loop, append the character at the current location to the new string we initialized earlier
Return the new string
"""

def every_other_letter(str):
    new_str = ""
    for l in str[::2]:
        if l not in new_str:
            new_str = new_str + l
        else: pass
    return new_str

print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))



"""
A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says 
“Belly Jeans” instead of “Jelly Beans”. Make a function that is similar, but instead of using the first syllable, switch the first character of two words. 

Define the function to accept two parameters for our two words
Get the first character of the first word and the first character of the second word
Get the remaining characters of the first word and the remaining characters of the second word.
Append the first character of the second word to the remaining character of the first word
Append a space character
Append the first character of the first word to the remaining characters of the second word.
Return the result
"""

def spoonerism(w1, w2):
    new_word = w2[0] + w1[1:] + " " + w1[0] + w2[1:]
    return new_word

print(spoonerism("Codecademy", "Learn"))
print(spoonerism("Jelly", "Beans"))
print(spoonerism("Hello", "world!"))



"""
A program that displays a large message on a blimp and fills in any missing space if a short phrase is provided. The function will accept a string 
and if the size is less than 20, it will fill in the remaining space with exclamation marks until the size reaches 20. If the 
provided string already has a length greater than 20, then we will simply return the original string. 

Define the function to accept one parameter for our string
Loop while the length of our input string is less than 20
Inside the loop, append an exclamation mark
Once done, return the result
"""

def add_exclamation(message):
    while len(message) < 20:
        message = message + "!"
    return message

print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))