string1=input("Enter a string:")    #getting a string
for number in range(0,len(string1)):
    if(number+1==len(string1)):
        break
    if(string1[number]=='A'): #finding the first 'A'
        temp=number+1
        break
for number1 in range(temp,len(string1)):    #Printing everything in between till last 'A' is reached
    if(string1[number1]=='A'):
        break
    print(string1[temp+1])

