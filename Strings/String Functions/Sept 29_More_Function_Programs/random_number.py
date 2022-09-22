'''
4. write a function that generates a random number that is always divisible by the input number. 
For eg, if input is 5, the randome number function should only generate numbers 5,20, 15, 75, etc.
'''
import random

def random_number():
    return random.randrange(1000) #generating a random number

divisible_by_number=int(input("Enter a number:")) #getting input from the user, the divisor

for count in range(0,10):
    number=random_number()
    if number%divisible_by_number==0: #checking whether the random number is divisible by the user's input number
        print(number) #if ues printing the random number

'''
Output:
Enter a number:5
890
'''
'''
Enter a number:3
198
'''
'''
Enter a number:7
252
'''