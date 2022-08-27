word1=input("Enter a string:")
word=word1.upper()
A1_flag=0 #to check the presence of first A
A2_flag=0 #to check the presence of last A
for first in range (0,len(word)-1): #to find the first index
    if word[first]=='A':
        first_index=first
        A1_flag=1
        print(first_index)
        word=word.replace('A',' ')
        print(word[first_index])
        break

for last in reversed(range (0,len(word))): #to find the last index
    if word[last]=='A':
        last_index=last
        A2_flag=1
        print(last_index)
            #word.replace('A','')
        break

if A1_flag and A2_flag: #printing letters between first and last index
    for number in range(first_index+1,last_index):
        print(word[number])
elif A1_flag:
    print("There is no last A in the word")
elif A2_flag:
    print("There is no first A in the word")
else:
    print("There is no A in the word")

'''Output:
Enter a string:abbbaaa
B
B
B
A
A'''
'''Enter a string:bbbb
There is no A in the word'''
