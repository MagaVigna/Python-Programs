items=["Sandwich","Pizza","Burger","Coffee"]
price=[100,150,200,50]
supply=[30,20,40,50]
sales=[]
print("Menu")
for menu in range(0,len(items)):
    print(items[menu],"-",price[menu])
for i in range(0,len(items)):
    print("Enter the number of",items[i],":")
    sale=int(input())
    sales.append(sale)

