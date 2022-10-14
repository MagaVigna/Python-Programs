# declaring items in the cafe  
items = {"Sandwich":
         {"Price": 100,# declaring the price of the items
          "Supply": 30, # declaring the supplies
          "Sales":0
          },
         "Pizza":
         {"Price": 150,
          "Supply": 20,
          "Sales":0
          },
         "Burger":
         {"Price": 200,
          "Supply": 40,
          "Sales":0
          },
         "Coffee":
         {"Price": 50,
          "Supply": 50,
          "Sales":0
          }
        }

menu_choice = 'yes'
trans = 10
total_sales = 0
while (trans > 0 and menu_choice == 'yes'):
    print("Menu")
    for menu in items.keys():
        print(menu, "-", items[menu]["Price"])  # printing the menu
    for index in items.keys():
        print("Enter the number of", index, ":")
        choice = int(input())
        items[index]["Sales"]=choice
        # checking if the item is available or not
        if (items[index]["Sales"]<= items[index]["Supply"] and choice != 0):
            total_sales += items[index]["Sales"]*items[index]["Price"]# calculating total sales
    trans -= 1
    menu_choice = input("Do you want to continue(Type yes):")

print("Sales of the cafe is:", total_sales)

'''
Output:
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
10
Enter the number of Coffee :
10
Do you want to continue(Type yes):no
Sales of the cafe is: 5000
'''