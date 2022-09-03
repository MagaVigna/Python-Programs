'''Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists.'''

fruits_quantity_list=[["apple","banana","orange","grapes"],["one","two","three","four","five","six","seven","eight","nine"]]
for menu in range(0,4):
    print(menu+1," ",fruits_quantity_list[0][menu]) #printing the menu
print(fruits_quantity_list[0])
order=input("What do you wanna buy?") #getting input from user
fruit_found=0
quantity_found=0
new_order=list(order.split(" ")) #converting the entered string into list of strings
for item in new_order:
    if item in fruits_quantity_list[0]: #checking if the input string has any fruit in it
        ordered_fruit=item
        fruit_found=1
    if item in fruits_quantity_list[1]:#checking if the input string has quantity mentioned
        ordered_quantity=item
        quantity_found=1

if fruit_found and quantity_found: #if fruit and quantity found printing those
    print("So you need",ordered_quantity,"number of",ordered_fruit)

elif fruit_found: #if only fruit found asking for quantity
    get_quantity=input("how many do you want?")
    print("So you need",get_quantity,"number of",ordered_fruit)

'''Output:
1   apple
2   banana
3   orange
4   grapes
What do you wanna buy?i want one apple
So you need one number of apple
'''
'''
1   apple
2   banana
3   orange
4   grapes
What do you wanna buy?apple
how many do you want?one
So you need one number of apple'''

'''
1   apple
2   banana
3   orange
4   grapes
What do you wanna buy?i want apple
how many do you want?two
So you need two number of apple'''