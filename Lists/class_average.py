
no_of_students=int(input("Enter the total number of students:"))
name_of_student=[]
marks_of_student=[]
for student in range (0,no_of_students):
    name=input("Enter your name:")
    name_of_student.append(name)
name_of_student.reverse()
for student in range(0,no_of_students):
    print("Enter your mark",name_of_student[student],": ")
    mark=int(input())
    marks_of_student.append(mark)
total=sum(marks_of_student)
class_average=total/no_of_students
print("Class average is:",class_average)
    