mark1=int(input("Enter the mark 1:"))
mark2=int(input("Enter the mark 2:"))
mark3=int(input("Enter the mark 3:"))
mark4=int(input("Enter the mark 4:"))
mark5=int(input("Enter the mark 5:")) #getting all the marks from the user
total=(mark1+mark2+mark3+mark4+mark5)/5
total1=(mark1+mark2+mark3+mark4)/4
total2=(mark1+mark2+mark3)/3
total3=(mark1+mark2)/2        #calculaing percentages seperately cause in the problem the condition requires average of 3 or ore subjects
total4=(mark1)/1
if(total==60):  #printing either pass or fail
    print("Pass")
elif((total1>=90 or total1>=75) and (total4>=50 or total4>=40)):
    print("Pass")
elif((total2>=90 or total2>=75) and (total3>=40 or total3>=50)):
    print("Pass")
else:
    print("Fail")