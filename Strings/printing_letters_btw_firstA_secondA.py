word1=input("Enter a string:")
word=word1.upper()
first_index=0
A1_flag=0 #to check the presence of first A
A2_flag=0 #to check the presence of second A
for first in range (0,len(word)-1): #to find the first index
    if word[first]=='A':
        first_index=first
        A1_flag=1
        break

for second in range (0,len(word)): #to find the second index
    if word[second]=='A' and first_index!=second:
        second_index=second
        A2_flag=1
        break

if A1_flag and A2_flag: #printing letters between first and second index
    for number in range(first_index+1,second_index):
        print(word[number])
elif A1_flag:
    print("There is no second A in the word")
elif A2_flag:
    print("There is no first A in the word")
else:
    print("There is no A in the word")

'''Output:
Enter a string:abbaa
B
B'''
'''Enter a string:Abaaa
B'''
'''Enter a string:abb
There is no second A in the word'''
'''Enter a string:bba
There is no first A in the word'''
''''Enter a string:bbb
There is no A in the word'''
