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
