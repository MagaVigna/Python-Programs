coffee=100 #coffee rate
coffee_count=0
vadai=100 #vadai rate
vadai_count=0
sandwich=200 #sandwich rate
sandwich_count=0
coke=60
coke_count=0 #coke rate
bill=0
menu_choice="yes"
while(menu_choice=="yes"): #displaying the menu
    print("Menu")
    print("1. Coffee - Rs 100")
    print("2. Vadai(1) - Rs 100")
    print("3. Sandwish - Rs 200")
    print("4. Coke - Rs 60")
    choice=int(input("Enter your choice:"))
    if choice==1:
        bill+=coffee
        coffee_count+=1
    elif choice==2:
        bill+=vadai
        vadai_count+=1
    elif choice==3:
        bill+=sandwich
        sandwich_count+=1
    elif choice==4:
        bill+=coke
        coke_count+=1
    menu_choice=input("Do you want to continue(Type yes):")
if(sandwich_count>1 or vadai_count>2): #calculating discounts
    coffee_discount=50
    if(coffee_count>0):
        while(coffee_count>0):
            bill-=coffee_discount
            coffee_count-=1
if(sandwich_count==1 and vadai_count==1 and coke_count==1 and coffee_count==1):
    bill=bill*0.2
if(bill>1000):
    bill=bill*0.2
print("Total cost is:",bill)
