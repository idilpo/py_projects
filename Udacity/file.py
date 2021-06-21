# opening a file
f = open('some_file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)


# writing to a file:
file = open('another_file.txt', 'w')
file.write()
file.close()


# auto closing the file w with: (cannot access f out of the block but can access the info)
with open('another_another_file.txt', 'r') as file1:
    file_info = file1.read()
print(file_info)

