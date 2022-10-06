file=open("C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\input_cafe.csv","r") #opening the csv file in reading mode
file_line=file.readline() #reading single line from the file
supply=[]
price=[]
items=[]
while file_line:
    linelist=file_line.split(",") #converting the line into list
    item_column=linelist[0]
    itemlist=item_column.split("\n")
    for index in itemlist: #storing only the numeric values
        items.append(index)
    print(items)
    if "Item_name" in items:
        items.remove("Item_name")
    supply_column=linelist[1]
    supply_list=supply_column.split("\n")
    for index in supply_list: #storing only the numeric values
        if index.isnumeric():
            supply.append(index)
    price_column=linelist[2] #seperating and storing the values from the selling_price column
    pricelist=price_column.split("\n") #converting the values into list
    for index in pricelist: #storing only the numeric values
        if index.isnumeric():
            price.append(index)
    file_line=file.readline()
print(item_column)
print(supply)
print(price)
temp_supply=supply
sales=[] #to store the sales of the day
stock_count=0 #to keep track on how many times the supply have been restocked
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
            if(int(sales[elements])<=int(supply[elements]) and choice!=0): #checking if the item is available or not
                total_sales+=sales[elements]*int(pricelist[elements])#calculating total sales
                supply[elements]-=sales[elements]
        for index in range(0,len(supply)):
            if (int(supply[index])<=int(sales[index]*0.2)): #cheking if sales went down to 20%
                stock_count=stock_count+1
                restock(supply[index],sales[index])     
        trans-=1
        menu_choice=input("Do you want to continue(Type yes):")
    print("Total number of items sold:",sales)
    print("Sales of the cafe is:",total_sales)
    print("The supply have been restocked",stock_count,"times")

def restock(supply,sales):
    while supply!=sales:
        supply+=1
        
sales_func()