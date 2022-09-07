''' In the input, find the first A and last A, print all the letters between these two A. 
  If there is no A or 2nd A is not found, find the first B  and last B and print all the letters between these two B. 
  If there is no B or 2nd B is not found, find the first C and last C and print all the letters between these two C. 
  Use functions.'''

from audioop import reverse


def finding_first_index(input_string,letter):
    input_string=input_string.upper()
    first_index=-1
    first_flag=0 #to check the presence of first letter
    for first in range (0,len(input_string)-1): #to find the first index of A,B,C
        if input_string[first]==letter:
            first_index=first
            first_flag=1
            break
    return [first_index,first_flag]

def finding_last_index(input_string,letter,first_index):
    input_string=input_string.upper()
    second_flag=0#to check the presence of last letter
    last_index=-1
    for last in reversed(range (0,len(input_string))): #to find the last index A,B,C
        if input_string[last]==letter and last!=first_index:
            last_index=last
            second_flag=1
            break
    return [last_index,second_flag]   

def finding_and_printing_letters_btw():#printing letters between first and last index
    word=input("Enter a string:")
    reversed_word=word[::-1]
    if 'a' in word and 'a' in reversed_word:
        first_list=finding_first_index(word,'A')
        last_list=finding_last_index(word,'A',first_list[0])
        letter='A'

    elif 'b' in word and 'b' in reversed_word:
        first_list=finding_first_index(word,'B')
        last_list=finding_last_index(word,'B',first_list[0])
        letter='B'
        
    elif 'c' in word and 'c' in reversed_word:
        first_list=finding_first_index(word,'C')
        last_list=finding_last_index(word,'C',first_list[0])
        letter='C'

    if first_list[1] and last_list[1]: #printing letters between first and last index
        for number in range(first_list[0]+1,last_list[0]):
            print(word[number])
        exit()
    elif first_list[1]:
        print("There is no last",letter, "in the word")
    elif last_list[1]:
        print("There is no first",letter, "in the word")

finding_and_printing_letters_btw()


'''
Output:
Enter a string:anna
n
n'''
'''
Enter a string:bnnb
n
n'''
