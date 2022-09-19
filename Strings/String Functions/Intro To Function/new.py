fruits_in_shop = ["Apple","Banana","Orange"]
inventory_count = [10,20,20]
min_of_inventory = [5,10,8]
reorder_inventory = [5,10,4]
fruits_name = ""
end = None

def fruit_index(fruits_name):
    for i in range (0,len(fruits_in_shop)):
        if fruits_name == fruits_in_shop[i]:
            return i

def maintain_inventory(index,sales_count):
    inventory_count[index] -= int(sales_count)

def reorder_inventory_function(index):
    if(inventory_count[index]<=min_of_inventory[index]):
        print("You need to reorder",fruits_in_shop[index],reorder_inventory[index])
        inventory_count[index]+=reorder_inventory[index]
    

while (fruits_name!="done"):
    fruits_name = input("Enter your fruit and enter done when complete: ")
    if (fruits_name == "done"):
        break
    sales_count = input("Enter how many do you want: ")
    print(fruits_name,sales_count)
    index = fruit_index(fruits_name)
    print("The index is: ",index)
    print(*inventory_count)
    maintain_inventory(index,sales_count)
    print(*inventory_count)
    reorder_inventory_function(index)
    print(*inventory_count)