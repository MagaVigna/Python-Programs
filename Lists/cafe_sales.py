items=["Sandwich","Pizza","Burger","Coffee"] #declaring items in the cafe
price=[100,150,200,50] #declaring the price of the items
supply=[30,20,40,50]    #declaring the supplies
sales=[]
menu_choice='yes'
trans=10
total_sales=0
while(trans>0 and menu_choice=='yes'):
    print("Menu")
    for menu in range(0,len(items)):
        print(items[menu],"-",price[menu]) #printing the menu
    for i in range(0,len(items)):
        print("Enter the number of",items[i],":")
        choice=int(input())
        sales.append(choice)
        if(sales[i]<=supply[i] and choice!=0): #checking if the item is available or not
            total_sales+=sales[i]*price[i]#calculating total sales
    trans-=1
    menu_choice=input("Do you want to continue(Type yes):")

print("Sales of the cafe is:",total_sales)

'''Output:
Menu
Sandwich - 100
Pizza - 150
Burger - 200
Coffee - 50
Enter the number of Sandwich :
1
Enter the number of Pizza :
2
Enter the number of Burger :
0
Enter the number of Coffee :
0
Do you want to continue(Type yes):yes
Menu
Sandwich - 100
Pizza - 150
Burger - 200
Coffee - 50
Enter the number of Sandwich :
1
Enter the number of Pizza :
2
Enter the number of Burger :
0
Enter the number of Coffee :
0
Do you want to continue(Type yes):no
Sales of the cafe is: 800
'''
'''Menu
Sandwich - 100
Pizza - 150
Burger - 200
Coffee - 50
Enter the number of Sandwich :
1
Enter the number of Pizza :
1
Enter the number of Burger :
1
Enter the number of Coffee :
1
Do you want to continue(Type yes):no
Sales of the cafe is: 500'''

'''Menu
Sandwich - 100
Pizza - 150
Burger - 200
Coffee - 50
Enter the number of Sandwich :
0
Enter the number of Pizza :
0
Enter the number of Burger :
0
Enter the number of Coffee :
0
Do you want to continue(Type yes):no
Sales of the cafe is: 0'''
