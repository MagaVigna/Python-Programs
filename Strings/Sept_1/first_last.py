'''Input a string. Print first and last char, add a comma, then print second and last but first char and so on.
   eg - input ABCD1234 , output - A4,B3,C2,D1. 
   Hint - use only one for loop. '''

input_string=input("Enter any string:") #getting the input string from the user
temp=int(len(input_string)-1)
for index in range(0,int(len(input_string))):
    if index==len(input_string)/2: #stopping the loop if the index value exceeds the half the value of stirng length
        break
    print(input_string[index],input_string[temp],",") #printing first and last char
    temp-=1
'''Output:
Enter any string:abcd1234 
a 4 ,
b 3 ,
c 2 ,
d 1 ,
'''
'''Enter any string:dcba4321
d 1 ,
c 2 ,
b 3 ,
a 4 ,'''
