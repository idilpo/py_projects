def createStudent(name, age, grades=None):
    if grades is None:
        grades = []
    return {
        'name': name,
        'age': age,
        'grades': grades
    }

def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])


chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)
addGrade(chrisley, 90)
addGrade(dallas, 100)