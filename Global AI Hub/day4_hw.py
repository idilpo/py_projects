# Create 5 students. Ask these students from the user.
# Each of these students should have a midterm grade, project grade and final grade.
# passingGrade = midterm * (0.3) + project * (0.3) + final * (0.4) passing grade should be determined like this.
# Create a dictionary that keeps these students’ information.
# Calculate the students’ grades and transfer them to the list with the help of indexing.
# Finally, set the student with the highest grade to be in the first index and the student
# with the lowest grade to be in the last index of the list.


#Comment: used way too many variables, would appreciate feedback on other ways involving lesser variable declarations.
midterm1, project1, final1 = input("Please enter the midterm, project and final grades of the first student (respectively): ").split()
grades1 = midterm1, project1, final1
grades_list1 = [float(i) for i in list(grades1)] # tuple is turned into a list containing grades
passing_grade1 = grades_list1[0] * 0.3 + grades_list1[1] * 0.3 + grades_list1[2] * 0.4
print("First student's passing grade is:", passing_grade1)


midterm2, project2, final2 = input("Please enter the midterm, project and final grades of the second student (respectively): ").split()
grades2 = midterm2, project2, final2
grades_list2 = [float(i) for i in list(grades2)]
passing_grade2 = grades_list2[0] * 0.3 + grades_list2[1] * 0.3 + grades_list2[2] * 0.4
print("Second student's passing grade is: ", passing_grade2)

midterm3, project3, final3 = input("Please enter the midterm, project and final grades of the third student (respectively): ").split()
grades3 = midterm3, project3, final3
grades_list3 = [float(i) for i in list(grades3)]
passing_grade3 = grades_list3[0] * 0.3 + grades_list3[1] * 0.3 + grades_list3[2] * 0.4
print("Third student's passing grade is: ", passing_grade3)

midterm4, project4, final4 = input("Please enter the midterm, project and final grades of the fourth student (respectively): ").split()
grades4 = midterm4, project4, final4
grades_list4 = [float(i) for i in list(grades4)]
passing_grade4 = grades_list4[0] * 0.3 + grades_list4[1] * 0.3 + grades_list4[2] * 0.4
print("Fourth student's passing grade is: ", passing_grade4)

midterm5, project5, final5 = input("Please enter the midterm, project and final grades of the fifth student (respectively): ").split()
grades5 = midterm5, project5, final5
grades_list5 = [float(i) for i in list(grades5)]
passing_grade5 = grades_list5[0] * 0.3 + grades_list5[1] * 0.3 + grades_list5[2] * 0.4
print("Fifth student's passing grade is: ", passing_grade5)


student_info = {'student1' : passing_grade1,
                'student2' : passing_grade2,
                'student3' : passing_grade3,
                'student4' : passing_grade4,
                'student5' : passing_grade5
}

list_of_grades = [] # an empty list is created
for i in student_info:
    list_of_grades.append(student_info[i]) # grades are added to the empty list
print("List of passing grades from the 1st student to the 5th:", list_of_grades)
list_of_grades.sort(reverse=True)
print("Sorted list of passing grades in decending order:", list_of_grades)
