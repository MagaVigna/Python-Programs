number=10
total=0
count=0
while(number!=0):
    number=int(input("Enter a number (0 to Stop): "))
    if (number==0):
        break
    count+=1
    total+=number
    average=total/count
print("The average of the entered numbers is: ",average)