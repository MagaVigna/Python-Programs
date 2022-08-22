items=["Sandwich","Pizza","Burger","Coffee"] #declaring items in the cafe
price=[100,150,200,50] #declaring the price of the items
supply=[30,20,40,50]    #declaring the supplies
sales=[]
print("Menu")
for menu in range(0,len(items)):
    print(items[menu],"-",price[menu]) #printing the menu
for i in range(0,len(items)):
    print("Enter the number of",items[i],":")
    choice=int(input())
    sales.append(choice)
    if(sales[i]<=supply[i]): #checking if the item is available or not
        total_sales=sales[i]*price[i] #calculating total sales
    else:
        print("Out of stock")
print("Sales of the cafe is:",total_sales)

'''Output:
Menu
Sandwich - 100
Pizza - 150
Burger - 200
Coffee - 50
Enter the number of Sandwich :
2
Enter the number of Pizza :
0
Enter the number of Burger :
0
Enter the number of Coffee :
1
Sales of the cafe is: 50'''