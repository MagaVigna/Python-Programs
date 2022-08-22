string1=input("Enter an string:") #getting two strings as input from the user
string2=input("Enter an string:")
for str1 in range(0,len(string1)): #comparing the charecters of the first string with every charecter of second string
    for str2 in range(0,len(string2)):
        if string1[str1]==string2[str2]:
            print(string1[str1])
            break
    
'''Output:
Enter an string:Hello
Enter an string:Hai
H'''