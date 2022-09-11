'''Write an app for the cafe. Calculate the sales for the day. 
Use a function to calculate each customer sale. Also, Use the function to restock the supply of items if the supply 
goes down to 20% of the original supply. Print how many times the supply was restocked. 
Also print the total numbers of items sold.
(Previous HW had the instructions for running a cafe. You can use that as a starting point)'''

items=["Sandwich","Pizza","Burger","Coffee"] #declaring items in the cafe
price=[100,150,200,50] #declaring the price of the items
supply=[30,20,40,50]    #declaring the supplies
sales=[] #to store the sales of the day
#stock_count=0 #to keep track on how many times the supply have been restocked
def menu():
        for menu in range(0,len(items)):
            print(items[menu],"-",price[menu]) #printing the menu
        
def sales_func():
    menu_choice='yes'
    stock_count=0 #to keep track on how many times the supply have been restocked
    trans=10 #maximum number of transaction
    total_sales=0
    while(trans>0 and menu_choice=="yes"):
        menu()
        for elements in range(0,len(items)):
            print("Enter the number of",items[elements],":")
            choice=int(input())
            sales.append(choice)
            if(sales[elements]<=supply[elements] and choice!=0): #checking if the item is available or not
                total_sales+=sales[elements]*price[elements]#calculating total sales
                supply[elements]-=sales[elements]
        for index in range(0,len(supply)):
            if supply[index]<=supply[index]*0.2:
                stock_count=stock_count+1
                restock(supply,sales)     
        trans-=1
        menu_choice=input("Do you want to continue(Type yes):")
    print("Total number of items sold:",sales)
    print("Sales of the cafe is:",total_sales)
    print("The supply have been restocked",stock_count,"times")

def restock(supply,sales):
    for index in range(0,len(supply)):
        sales[index]+=supply[index]
        
sales_func()


'''Output:
Menu
Sandwich - 100
Pizza - 150
Burger - 200
Coffee - 50
Enter the number of Sandwich :
10
Enter the number of Pizza :
10
Enter the number of Burger :
19
Enter the number of Coffee :
10
Do you want to continue(Type yes):no
Sales of the cafe is: 6800
The supply have been restocked 0 times'''
'''
Menu
Sandwich - 100
Pizza - 150
Burger - 200
Coffee - 50
Enter the number of Sandwich :
20
Enter the number of Pizza :
20
Enter the number of Burger :
20
Enter the number of Coffee :
20
hekko
Do you want to continue(Type yes):no
Sales of the cafe is: 10000
The supply have been restocked 1 times'''


