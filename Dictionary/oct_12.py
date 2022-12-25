# declaring items in the cafe
items = ["Sandwich", "Pizza", "Burger", "Coffee"]
price = [100, 150, 200, 50]  # declaring the price of the items
supply = [30, 20, 40, 50]  # declaring the supplies
sales = []
items = {"sandwich":
         {"quantity": 30,
          "price": {"morning":100, "evening":150},
          "temperature":{"hot","cold"},

         "pizza":
         {"quantity": 20,
          "morning_price": 150,
          "evening_price":100}}
menu_choice = 'yes'
trans = 10
total_sales = 0
while (trans > 0 and menu_choice == 'yes'):
    print("Menu")
    for menu in range(0, len(items)):
        print(items[menu], "-", price[menu])  # printing the menu
    for i in range(0, len(items)):
        print("Enter the number of", items[i], ":")
        choice = int(input())
        sales.append(choice)
        # checking if the item is available or not
        if (sales[i] <= supply[i] and choice != 0):
            total_sales += sales[i]*price[i]  # calculating total sales
    trans -= 1
    menu_choice = input("Do you want to continue(Type yes):")

print("Sales of the cafe is:", total_sales)
