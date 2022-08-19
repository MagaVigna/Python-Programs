coffee_cost=100 #coffee rate
coffee_count=0
vadai_cost=100 #vadai rate
vadai_count=0
sandwich_cost=200 #sandwich rate
sandwich_count=0
coke_cost=60 #coke rate
coke_count=0 
bill=0
discount_applied=False
menu_choice="yes"
while(menu_choice=="yes"): #displaying the menu
    print("Menu")
    print("1. Coffee - Rs 100")
    print("2. Vadai(1) - Rs 100")
    print("3. Sandwich - Rs 200")
    print("4. Coke - Rs 60")
    choice=int(input("Enter your choice:"))
    if choice==1:
        coffee_count=int(input("Enter the number of coffees:"))
    elif choice==2:
        vadai_count=int(input("Enter the number of vadais:"))
    elif choice==3:
        sandwich_count=int(input("Enter the number of sandwich:"))
    elif choice==4:
        coke_count=int(input("Enter the number of coke:"))
    else:
        print("Invalid Input")
    menu_choice=input("Do you want to continue(Type yes):")
bill=(coffee_cost*coffee_count)+(vadai_cost*vadai_count)+(sandwich_cost*sandwich_count)+(coke_cost*coke_count)
if(sandwich_count>1 or vadai_count>2): #calculating discounts
    coffee_discount=50
    print("Since you have brought more than one sandwich or more than two vadais your coffee rate is Rs50")
    bill=(coffee_discount*coffee_count)+(vadai_cost*vadai_count)+(sandwich_cost*sandwich_count)+(coke_cost*coke_count)
if(sandwich_count>=1 and vadai_count>=1 and coke_count>=1 and coffee_count>=1):
    bill-=bill*0.2
    discount_applied=True
if((bill>1000) and (not discount_applied)):
    bill-=bill*0.2
print("Total cost is:",bill)
