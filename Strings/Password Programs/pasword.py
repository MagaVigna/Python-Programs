passwrd=input("Enter your password:")
SpecialSym =['$', '@', '#', '%']
alpha_count=0
splchar_count=0
digit_count=0
length=len(passwrd)
if(len(passwrd)>=8):
    for index in range(0,len(passwrd)):
        if (passwrd[index].isdigit()):
            digit_count+=1
        elif (passwrd[index].isalpha()):
            alpha_count+=1
        elif any(char in SpecialSym for char in passwrd):
            splchar_count+=1
    if((digit_count>=1 and alpha_count>=1 and splchar_count>=1) and length>=16):
        print("Very Strong")
    elif(digit_count>=2 and alpha_count>=3 and splchar_count>=1):
        print("Strong")
    elif(digit_count>=1 and alpha_count>=1 and splchar_count>=1):
        print("Ok")
    elif(digit_count==length or alpha_count==length or splchar_count==length):
        print("Weak")
    else:
        print("Invalid")
else:
    print("Minimum number of charecters is 8")

'''Outputs:
Enter your password:abcdefghij321#2@
Very Strong'''
'''Enter your password:abcd12@#
Strong'''
'''Enter your password:abcdef1#
Ok'''
'''Enter your password:abcdefgh
Weak'''
'''Enter your password:abcdefg1
Invalid'''
'''Enter your password:abcd
Minimum number of charecters is 8'''