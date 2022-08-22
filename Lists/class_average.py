
no_of_students=int(input("Enter the total number of students:")) #getting number of students as input
name_of_student=[]
marks_of_student=[]
for student in range (0,no_of_students):
    name=input("Enter your name:") #getting names from first to last
    name_of_student.append(name)
name_of_student.reverse() #reversing the list
for student in range(0,no_of_students):
    print("Enter your mark",name_of_student[student],": ")
    mark=int(input()) #getiing the marks in reverse order
    marks_of_student.append(mark)
total=sum(marks_of_student)
class_average=total/no_of_students #calculating average
print("Class average is:",class_average)
'''Output:
Enter the total number of students:3
Enter your name:Maga
Enter your name:Vigna
Enter your name:Gokul
Enter your mark Gokul : 
100
Enter your mark Vigna : 
90
Enter your mark Maga : 
80
Class average is: 90.0'''
    