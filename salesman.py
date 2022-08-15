phones_sold=int(input("Enter the number of phones sold in the month: ")) #number of phones he sold
salary=0
total=0
while(salary<12000): #to calculate his salary according to his comission
    salary=salary+1000
    if(salary==12000):
        break
    if(phones_sold>=5):
        salary=salary+100
    elif (phones_sold>=10):
        salary=salary+200
for i in range(1,13): #loop to find the everage
    total=total+salary
average=total/12
print("His monthly salary:", salary)
print("His average salary per month in one year is: ",average)