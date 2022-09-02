
'''Input a string. 
    Print all the chars that are in Odd index - eg intput - abcd, output bd
    Print all the chars in the even index in reverse order - eg input abcd output ca'''

input_string=input("Enter any string:") #getting the input string
print("The charecters in the odd indexes:")
for odd_index in range(1,len(input_string),2): #loop to print the values in odd indexes
    print(input_string[odd_index])
print("The charecters in the even indexes:")
starting_index=-1
if (len(input_string)%2==0): #checking if the length of the string is even initialising variable to start the loop from second last index
    starting_index=len(input_string)-2
else: #else initialising variable to start from last index
    starting_index=len(input_string)-1
for even_index in range(starting_index,-1,-2):
    print(input_string[even_index])

'''Outputs:
Enter any string:1234
The charecters in the odd indexes:
2
4
The charecters in the even indexes:
3
1'''
'''The charecters in the odd indexes:
b
d
The charecters in the even indexes:
e
c
a'''