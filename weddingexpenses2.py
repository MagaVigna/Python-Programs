lunch=int(input("Enter the cost of lunch:")) #getting cost of lunch as input
guests=int(input("Enter the number of guests for the wedding:"))
breakfast=(lunch/2)*guests  #calculating next values according to the problem
hall=(lunch/3)*guests
decoration=(hall/2)*guests
parking=((hall*10)/100)*guests
print("Lunch cost is:",lunch)   #printing the found values
print("Breakfast cost is:",int(breakfast))
print("Hall cost:",int(hall))
print("Decorations cost:",int(decoration))
print("Parking cost:",int(parking))
total=lunch+int(breakfast)+int(hall)+int(decoration)+int(parking)
print("Total wedding epenses:",total)#printing total expenses
if((total/2)>50000):    #checking if loan is needed
    print("Bride needs to take a loan")
    print("She needs to take",(total/2)-50000)
else:
    print("Loan is not required")