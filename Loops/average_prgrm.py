number=10
total=0
count=0 #to continue till number becomes zero
while(number!=0): #to continue till number becomes zero 
    number=int(input("Enter a number (0 to Stop): ")) 
    if (number==0):
        break
    count+=1
    total+=number
    average=total/count #calculating average
print("The average of the entered numbers is: ",average)
