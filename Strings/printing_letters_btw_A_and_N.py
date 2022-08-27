word1=input("Enter a string:")
word=word1.upper()
A_flag=0
N_flag=0
for first in range (0,len(word)):
    if word[first]=='A':
        first_index=first
        A_flag=1
        break
    elif word[first]=='N':
        print("N comes before A")
        exit()

for last in reversed(range (0,len(word))):
    if word[last]=='N':
        last_index=last
        N_flag=1
        break

if A_flag and N_flag:
    for number in range(first_index+1,last_index):
        print(word[number])
elif A_flag:
    print("There is no N in the word")
elif N_flag:
    print("There is no A in the word")