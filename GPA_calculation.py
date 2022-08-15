total=0
for student in range(1,4):
    for subject in range(1,4):
        print("Enter the mark of subject ",subject," of student ",student)
        mark = int(input())
        total=total+mark
        if(mark<=100 and mark>=85):
            gpa=4
            print("GPA is: ",gpa)
        elif(mark<=84 and mark>=80):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=84 and mark>=80):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=79 and mark>=75):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=74 and mark>=70):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=69 and mark>=65):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=64 and mark>=60):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=59 and mark>=55):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=54 and mark>=50):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=49 and mark>=45):
            gpa=3.7
            print("GPA is: ",gpa)
        elif(mark<=44 and mark>=40):
            gpa=3.7
            print("GPA is: ",gpa)
        else:
            gpa=0
            print("GPA is: ",gpa)
average=total/3
print("The class average is: ",average)