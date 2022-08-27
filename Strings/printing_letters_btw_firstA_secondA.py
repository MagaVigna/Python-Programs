word1=input("Enter a string:")
word=word1.upper()
A1_flag=0
A2_flag=0
for first in range (0,len(word)):
    if word[first]=='A':
        first_index=first
        A1_flag=1
        break

for last in reversed(range (0,len(word))):
    if word[last]=='A':
        last_index=last
        A2_flag=1
        break

if A1_flag and A2_flag:
    for number in range(first_index+1,last_index):
        print(word[number])
else:
    print("There is no A in the word")
