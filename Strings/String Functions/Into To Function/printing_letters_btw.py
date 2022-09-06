''' In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
  Use functions.'''

def printing_letters_btw(input_string):
    input_string=input_string.upper()
    first_index=0
    A1_flag=0 #to check the presence of first A
    A2_flag=0 #to check the presence of last A
    B1_flag=0 #to check the presence of first B
    B2_flag=0 #to check the presence of last B
    C1_flag=0 #to check the presence of first C
    C2_flag=0 #to check the presence of last C
    for first in range (0,len(input_string)-1): #to find the first index of A,B,C
        if input_string[first]=='A':
            first_index=first
            A1_flag=1
            break
        elif input_string[first]=='B':
            first_index=first
            B1_flag=1
            break
        elif input_string[first]=='C':
            first_index=first
            C1_flag=1
            break

    for last in reversed(range (0,len(input_string))): #to find the last index A,B,C
        if input_string[last]=='A' and last!=first_index:
            last_index=last
            A2_flag=1
            break
        if input_string[last]=='B' and last!=first_index:
            last_index=last
            B2_flag=1
            break
        if input_string[last]=='C' and last!=first_index:
            last_index=last
            C2_flag=1
            break
    
    if A1_flag and A2_flag: #printing letters between first and last index
        for number in range(first_index+1,last_index):
            print(input_string[number])
        exit()
    elif A1_flag:
        print("There is no last A in the word")
    elif A2_flag:
        print("There is no first A in the word")


    if B1_flag and B2_flag: #printing letters between first and last index
        for number in range(first_index+1,last_index):
            print(input_string[number])
        exit()
    elif B1_flag:
        print("There is no last B in the word")
    elif B2_flag:
        print("There is no first B in the word")


    if C1_flag and C2_flag: #printing letters between first and last index
        for number in range(first_index+1,last_index):
            print(input_string[number])
        exit()
    elif C1_flag:
        print("There is no last C in the word")
    elif C2_flag:
        print("There is no first C in the word")
    else:
        print("There is no A,B,C in the input string")

word=input("Enter a string:")
printing_letters_btw(word)
'''
Output:
Enter a string:abbba
B
B
B'''
'''
Enter a string:baaab
A
A
A'''
'''
Enter a string:caaac
A
A
A'''
'''
Enter a string:gggg
There is no A,B,C in the input string'''