fruits=["apples","orange","other_fruits"] #declaring fruits names
days=["Monday","Tuesday","Wednesday"] 
supply=[]
price=[25,15,10]
for amount in range(0,len(fruits)):
    print("Enter the number of",fruits[amount],":") #getting the supply from the owner
    temp=int(input())
    supply.append(temp)
for count in range(0,len(fruits)): #calculating and printing the sales
    if days[count]=="Monday":
        sales=(((supply[0]*0.5)*price[0]) + ((supply[1]*0.5)*price[1]) + ((supply[2]-10)*price[2]))
        print("Sales of monday is:",sales)
    elif days[count]=="Tuesday":
        sales=((supply[0]*price[0]) + ((supply[1]*0.75)*price[1]) + ((supply[2]-30)*price[2]))
        print("Sales of tuesday is:",sales)
    elif days[count]=="Wednesday":
        sales=((supply[0]*price[0]) + (supply[1]*price[1]) + (supply[2]*price[2]))
        print("Sales of wednesday is:",sales)

'''Output:
Enter the number of apples :
100
Enter the number of orange :
100
Enter the number of other_fruits :
100
Sales of monday is: 2900.0
Sales of tuesday is: 4325.0
Sales of wednesday is: 5000'''

'''Enter the number of apples :
10
Enter the number of orange :
10
Enter the number of other_fruits :
10
Sales of monday is: 200.0
Sales of tuesday is: 162.5
Sales of wednesday is: 500'''

'''Enter the number of apples :
1000
Enter the number of orange :
1000
Enter the number of other_fruits :
1000
Sales of monday is: 29900.0
Sales of tuesday is: 45950.0
Sales of wednesday is: 50000'''