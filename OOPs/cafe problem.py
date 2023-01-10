class Dish:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cafe:
    def __init__(self):
        self.dishes = {}
        self.sales = {}

    def add_dish(self, dish):
        self.dishes[dish.name] = dish

    def add_sale(self, dish_name, quantity_sold):
        self.sales[dish_name] = quantity_sold

    def get_info(self, question):
        if question in self.dishes:
            return f"{question} - Price: {self.dishes[question].price}, Quantity: {self.dishes[question].quantity} ,Quantity sold: {self.sales[question]}"
        else:
            return f"I'm sorry, I don't have information on {question}."

# Create a cafe object
cafe = Cafe()

# Ask the manager for the available dishes and their prices and quantities
print("Enter the available dishes and their prices and quantities (Enter stop when finished):")
while True:
    dish_input = input("Enter dish name and price and quantity (e.g. vadai 10 20): ")
    if dish_input=='stop':
        # Exit the loop if stop is entered
        break
    
    # Split the input into dish name, price, and quantity
    dish_info = dish_input.split()
    dish_name = dish_info[0]
    price = int(dish_info[1])
    quantity = int(dish_info[2])
    
    # Create a dish object and add it to the cafe
    dish = Dish(dish_name, price, quantity)
    cafe.add_dish(dish)

# Ask for the sales for the day
print("Enter the sales for the day (Enter stop when finished):")
while True:
    sales_input = input("Enter sales data (e.g. vadai 10): ")
    if sales_input=='stop':
        # Exit the loop if stop is entered
        break
    
    # Split the input into dish name and quantity sold
    sales_info = sales_input.split()
    dish_name = sales_info[0]
    quantity_sold = int(sales_info[1])
    
    # Add the sales data to the cafe
    cafe.add_sale(dish_name, quantity_sold)

# Ask the owner what details they want to know
while True:
    question = input("I have the data. What details do you want to know? ")
    if not question:
        # Exit the loop if no input is entered
        break
    
    # Get the information from the cafe
    info = cafe.get_info(question)
    print(info)
