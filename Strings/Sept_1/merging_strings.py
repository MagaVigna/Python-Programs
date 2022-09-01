'''Input two strings. Output is both strings merged . Eg - input1 = ABCD, input 2 = 1234. Output = A1B2C3D4 '''

string1=input("Enter the first string:") #getting two strings as input from the user
string2=input("Enter the second string:")
temp=[] #to store the merged string
if len(string1)==len(string2): #if the length of both the strings are equal merging the strings
    for index in range (0,len(string1)):
        temp+=string1[index]+string2[index]
else: #else error message 
    print("The length of the strings are not equal")
print(*temp)

'''Output:
Enter the first string:abcd
Enter the second string:1234
a 1 b 2 c 3 d 4'''
'''Enter the first string:abcde
Enter the second string:123
The length of the strings are not equal'''