'''Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Then ask the cusomter how many of that fruit s/he wants. Customer can say 'one' or 'I want one' or 'just one' 
or something like that.
Print the quantity tha customer asks for.
Continue asking fruit/quantity of fruit until the customer says 'That's all' or 'No more'.
You can limit the quantity to single digit number.
Use functions. Use the same function to get the fruit name and also the quantity.'''

def fruit_vendor():
    choice="yes"
    while (choice!="That's all" and choice!="No more"): #to execute till the users says thats all
        fruits_quantity_list=[["apple","banana","orange","grapes"],["one","two","three","four","five","six","seven","eight","nine"]]
        for menu in range(0,len(fruits_quantity_list[0])):
            print(menu+1," ",fruits_quantity_list[0][menu]) #printing the menu
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
            get_quantity=list(get_quantity.split(" "))
            for char in fruits_quantity_list[1]:
                if get_quantity[len(get_quantity)-1]== char: #finding the number of quantity
                    print("So you need",char,"number of",ordered_fruit)
        choice=input("Do you want to continue, If no, Type That's all or No more:")

    
fruit_vendor()
'''
Output:
1   apple
2   banana
3   orange
4   grapes
What do you wanna buy?apple
how many do you want?one
So you need one number of apple
Do you want to continue, If no, Type That's all or No more:yes
1   apple
2   banana
3   orange
4   grapes
What do you wanna buy?orange
how many do you want?i want one
So you need one number of orange
Do you want to continue, If no, Type That's all or No more:No more'''
'''
1   apple
2   banana
3   orange
4   grapes
What do you wanna buy?apple
how many do you want?one
So you need one number of apple
Do you want to continue, If no, Type That's all or No more:No more'''