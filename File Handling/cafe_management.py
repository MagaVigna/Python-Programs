import csv
supply=[] #initialising necessary variables
price=[]
items=[]
menu_var=[]
temp_supply=supply
sales=[] #to store the sales of the day
stock_count=0 #to keep track on how many times the supply have been restocked

def reading_data_from_file():
    file=open("C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\input_cafe.csv","r") #opening the csv file in reading mode
    csv_reader=csv.reader(file)
    item_index=0
    supply_index=1
    price_index=2
    next(csv_reader)
    for line in csv_reader:
        menu_var.append(line)
    for index in range(0,len(menu_var[0])):
        items.append(menu_var[index][item_index])
        supply.append(int(menu_var[index][supply_index]))
        price.append(menu_var[index][price_index])
    print(items)
    print(supply)
    print(price)
    file.close()

def writing_data_into_file():
    with open("C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\Output_cafe.csv", "w",encoding='UTF8', newline='') as csv_file: #opening file in write mode
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Items_name', 'Sales']) #writing the header data
        for index in range(0, len(items)):
            writer.writerow([items[index],sales[index]]) #writing the values
    csv_file.close()

def printing_data_from_output_file():
    with open("C:\\Users\\Maga Vigna\\Desktop\\College\\Sayur\\Output_cafe.csv", "r",encoding='UTF8', newline='') as csv_file:
        csvFile = csv.reader(csv_file) 
        for lines in csvFile: 
            print(lines) 
    csv_file.close()

def menu():
    print("----------Menu------------")
    for menu in range(0,len(items)):
        print(items[menu],"-",price[menu]) #printing the menu
        
def sales_func():
    menu_choice='yes'
    stock_count=0 #to keep track on how many times the supply have been restocked
    trans=10 #maximum number of transaction
    total_sales=0
    while(trans>0 and menu_choice=="yes"):
        menu()
        for elements in range(0,len(supply)):
            print("Enter the number of",items[elements],":")
            choice=int(input())
            sales.append(choice)
            if(int(sales[elements])<=int(supply[elements]) and choice!=0): #checking if the item is available or not
                total_sales+=sales[elements]*int(price[elements])#calculating total sales
                supply[elements]-=sales[elements]
        for index in range(0,len(supply)):
            if (int(supply[index])<=int(sales[index]*0.2)): #cheking if sales went down to 20%
                stock_count=stock_count+1
                restock(supply[index],sales[index])     
        trans-=1
        menu_choice=input("Do you want to continue(Type yes):")
    print("The supply have been restocked",stock_count,"times")

def restock(supply,sales):
    while supply!=sales:
        supply+=1

reading_data_from_file()

sales_func()

writing_data_into_file()

printing_data_from_output_file()

'''
Output:
----------Menu------------
Vadai - 100
Pizza - 100
Coke - 50
Burger - 150
Sandwich - 80
Briyani - 200
Enter the number of Vadai :
10
Enter the number of Pizza :
10
Enter the number of Coke :
10
Enter the number of Burger :
10
Enter the number of Sandwich :
10
Enter the number of Briyani :
10
Do you want to continue(Type yes):no
Total number of items sold: [10, 10, 10, 10, 10, 10]
Sales of the cafe is: 6800
The supply have been restocked 0 times
'''