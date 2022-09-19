'''1. Write an app to calculate Grades for students in each subject.
Mark > 90 is A, > 80 is B, > 70 is C, > 60 is D. anything less than 60 is fail.
Write a function that returns the grade for one subject for all the students in the class.
Also, print the class avg grade.'''

total=0     #initialising total and average variable to store the class total mark and average
average=0
    
def grade_calculation(mark): #function to find the grade for the input mark
    if mark>90:
        print("Your grade is A")
    elif mark>80:
        print("Your grade is B")
    elif mark>70:
        print("Your grade is C")
    elif mark>=60:
        print("Your grade is D")
    else:
        print("Fail")
    

def average_calculation(): #calculating the class average
    global total
    total=total+mark
    global average
    average=total/no_of_students

no_of_students = int(input("Enter the total number of students in the class:"))

for students in range(0,no_of_students): #getting marks from every student and printing their corresponding grades
    mark=int(input("Enter the mark of the subject:"))
    grade_calculation(mark)
    average_calculation()

print("The class average is:") #printing the class average grade by passing the average as parameter to the grade calculation function
grade_calculation(average)
print(average)

'''Output:
Enter the total number of students in the class:3
Enter the mark of the subject:90
Your grade is B
Enter the mark of the subject:80
Your grade is C
Enter the mark of the subject:70
Your grade is D
The class average is:
Your grade is C
80.0'''
'''Enter the total number of students in the class:1
Enter the mark of the subject:100
Your grade is A
The class average is:
Your grade is A
100.0'''