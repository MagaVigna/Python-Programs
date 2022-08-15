i=10
number=10
count=0 #to count the number of students
while(i>=10 ): #loop to continue the next statements till i becomes 10 or number becomes 4
    print("OPINION POLL")
    print("Enter 1. for online class")
    print("2. in person class")
    print("3. mixed")
    print("4. No comment")
    number=int(input())
    if(number==4):
        break
    print("Enter Male or Female:") #to check the gender for further use
    gender=input()
    if(gender=="Female" and number==1):
        count=count+1
    i=i+1
print("The percentage of females who prefer online class is:",count)
