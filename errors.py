CV1 = {('Name', 'Age', 'Pronouns'): ('Idil', 20, 'she/her'),
        'Degree': 'BSc Computer Science',
       'Languages': ['Turkish', 'English', 'German', 'Spanish', 'Esperanto'],
       'Interests': ['playing tennis', 'learning languages', 'reading']}

for k,v in CV1.items():
       print(str(k) + ':' + str(v), end=', ')

print("\n--CV1--")
for key, value in CV1.items():
    print(key, ':', value)

