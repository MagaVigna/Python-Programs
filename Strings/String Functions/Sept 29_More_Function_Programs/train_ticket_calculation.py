'''2. Calculate the cost of train tickets. Single one way ticket from Madurai to Chennai (or vice versa) is Rs1000. 
Adding a return ticket will cost Rs750 extra.
Family of 4 or more gets 20% off. Senior rate is 50% off. '''

one_way_ticket=1000 #hard coding the values for one way and return tickets and the senior age
return_ticket=750
return_ticket_count=0
senior_age=60
name=''
age=0
choice=''
ticket=0
number_of_passengers=0
def get_details(): #function to get the user details
    global name,age,number_of_passengers,choice,return_ticket_count
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    choice=input("Do you want a return ticket (type y for yes):")
    if choice=='y':
        return_ticket_count+=1

def calc_ticket_cost():
    global ticket
    ticket=number_of_passengers*one_way_ticket #calculating the cost of one way ticket
    if choice=='y':
        ticket+=(return_ticket*return_ticket_count) #calculating the cost og return ticket
    if number_of_passengers>=4: #calculating the discounts for family of four or more
        ticket-=ticket*0.2
    if age>=senior_age: #calculating discount for the senior age passengers
        ticket-=ticket*0.5
    print(ticket)
number_of_passengers=int(input("Enter the number of passengers:"))
for index in range(0,number_of_passengers):
    print("Enter details of passenger ",index+1,":")
    get_details()
    calc_ticket_cost()
print("The total cost of the ticket is:",ticket) #printing the total ticket cost

'''Output:
Enter the number of passengers:4
Enter details of passenger  1 :
Enter your name:b
Enter your age:20
Do you want a return ticket (type y for yes):n
Enter details of passenger  2 :
Enter your name:b
Enter your age:20
Do you want a return ticket (type y for yes):n
Enter details of passenger  3 :
Enter your name:b
Enter your age:20
Do you want a return ticket (type y for yes):n
Enter details of passenger  4 :
Enter your name:b
Enter your age:20
Do you want a return ticket (type y for yes):n
The total cost of the ticket is: 3200.0'''


'''
Enter the number of passengers:1
Enter details of passenger  1 :
Enter your name:A
Enter your age:90
Do you want a return ticket (type y for yes):n
The total cost of the ticket is: 500.0'''

'''Enter the number of passengers:1
Enter details of passenger  1 :
Enter your name:A
Enter your age:90
Do you want a return ticket (type y for yes):y
875.0
The total cost of the ticket is: 875.0'''