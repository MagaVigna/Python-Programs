cakebuycost=20
cakesellcost=40
breadbuycost=10
breadsellcost=15
salary=200
customers=10    #intialising all the given values in variables
noofbreadbrought=input("Enter the amount of bread brought:")
noofcakebrought=input("Enter the amount of cake brought:")
cakestock=input("Enter the cake supply:")
breadstock=input("Enter the bread supply:")
for i in range(9): #loop for number of customers
    cakebuycost+=20
    breadbuycost+=10
    for x in range(int(noofcakebrought)): #loop for number of cake brought
        if(int(cakestock)>0):
            cakesellcost+=40   
        else:
            print("No cake Left") 
    for x in range(int(noofbreadbrought)): #loop for number of  bread brought
        if(int(breadstock)>0):
            breadsellcost+=15
        else:
            print("No bread left")
cakeprofit=cakebuycost-cakesellcost
breadprofit=breadbuycost-breadsellcost
profit=cakeprofit-breadprofit #calculationg profit from the sales
if(profit>salary):
    overallprofit=profit-salary
else:
    overallprofit=salary-profit
print("The profit is:",overallprofit)