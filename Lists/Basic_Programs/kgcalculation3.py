budget=int(input("Enter your budget:"))#getiing budget as input
petrol= int((budget/3)) #calculating petrol expenses
budget-=petrol  #calculatinf budget after minusing the petrol cost
total=0
print("Petrol expenses are:",petrol)
print("Budget after excluding petrol expenses:",budget)
for i in range(100):
    total+=30.5 #because onion=20 and toamto=10.5 
    if(total>budget):
        print(i,"kgs of onion and tomato can be brought")
        break
