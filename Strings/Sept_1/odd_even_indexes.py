
'''Input a string. 
    Print all the chars that are in Odd index - eg intput - abcd, output bd
    Print all the chars in the even index in reverse order - eg input abcd output ca'''

input_string=input("Enter any string:") #getting the input string
print("The charecters in the even indexes:")
for odd_index in range(1,len(input_string),2): #loop to print the values in odd indexes
    print(input_string[odd_index])
print("The charecters in the odd indexes:")
for even_index in range(0,len(input_string),2): #loop to print the values in even indexes
    print(input_string[even_index])

'''Outputs:
Enter any string:abcd
The charecters in the even indexes:
b
d
The charecters in the odd indexes:
a
c'''
'''The charecters in the even indexes:
e
l
The charecters in the odd indexes:
h
l
o'''