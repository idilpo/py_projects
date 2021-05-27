# HW2 – CV Application

# Create 5 dictionaries. Each dictionary should represent a CV.
# Create a CV containing the information of the 5 created people.
# Print the information on CV’s created on the screen.


# Comment: I wanted to group the keys "name", "age" and "pronouns" together with their values in a tuple at first.
# So, it was ('Name', 'Age', 'Pronouns'): ('Idil', 20, 'she/her') for each CV example.
# However I was not able to figure out how to remove the brackets when printing. Thus, changed it to how it is now .
# Would appreciate some feedback on the issue.

CV1 = {'Name': 'Idil', 'Age': 20, 'Pronouns': 'she/her',
        'Degree': 'BSc Computer Science',
       'Languages': ['Turkish', 'English', 'German', 'Spanish', 'Esperanto'],
       'Interests': ['playing tennis', 'learning languages', 'travelling']}

CV2 = {'Name': 'Ameer', 'Age' : 22, 'Pronouns': 'he/him',
        'Degree': 'BSc Veterinary Medicine',
       'Languages': ['Indian', 'English', 'Spanish', 'French'],
       'Interests': ['playing volleyball', 'running', 'dogs']}

CV3 = {'Name': 'Ada', 'Age': 20, 'Pronouns': 'she/her',
        'Degree': 'BSc Dentistry',
       'Languages': ['Turkish', 'English', 'German', 'French'],
       'Interests': ['cats', 'design', 'tiktok']}

CV4 = {'Name': 'Asad', 'Age' : 19, 'Pronouns': 'he/him',
        'Degree': 'BSc Computer Science',
       'Languages': ['Indian', 'English', 'Arabic', 'French'],
       'Interests': ['photography', 'gaming', 'skateboarding']}

CV5 = {'Name': 'Bianca', 'Age': 18, 'Pronouns': 'she/her',
        'Degree': 'BSc Medicine',
       'Languages': ['Chinese', 'English', 'Malay'],
       'Interests': ['crochet', 'makeup', 'fashion']}

print("\n--CV1--")
for key, value in CV1.items():
    print(key, ':', value)

print("\n--CV2--")
for key, value in CV2.items():
    print(key, ':', value)

print("\n--CV3--")
for key, value in CV3.items():
    print(key, ':', value)

print("\n--CV4--")
for key, value in CV4.items():
    print(key, ':', value)

print("\n--CV5--")
for key, value in CV5.items():
    print(key, ':', value)
