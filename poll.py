number_of_students=0
count=0 #to count the number of students
while(number_of_students<=10 ): #loop to continue the next statements till i becomes 10 or number becomes 4
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
    number_of_students+=1
percentage_of_online_females=(count/number_of_students)*100    

print("The percentage of females who prefer online class is:",percentage_of_online_females)

print("The percentage of females who prefer online class is:",percentage_of_online_females)

