word1=input("Enter a string:")
word=word1.upper()
A_flag=0 #to check if A is present in the word
N_flag=0 #to check if N is present in the word
N2_flag=0
for first in range (0,len(word)-1): #finding first index
    if word[first]=='A':
        first_index=first
        A_flag=1
        break
    if word[first]=='N':
        N_flag=1
        N2_flag=1
        break

for last in reversed(range (0,len(word))): #finding last index
    if word[last]=='N':
        last_index=last
        N_flag=1
        break
if N2_flag:
    print("N comes before A")
elif A_flag and N_flag: #printing letter between first and last index
    for number in range(first_index+1,last_index):
        print(word[number])
elif A_flag:
    print("There is no N in the word")
elif N_flag:
    print("There is no A in the word")
else:
    print("There is no A and N")

''' Output:
Enter a string:abbn
B
B'''

'''Enter a string:abb
There is no N in the word'''

'''Enter a string:bbn
There is no A in the word'''

'''Enter a string:nbba
N comes before A'''

'''Enter a string:bcde
There is no A and N'''
