'''Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long.
'''
passwrd=input("Enter your password:")
SpecialSym =['$', '@', '#', '%'] #declaring list for special charecters
alpha_count=0 #to count the number of alphabets
splchar_count=0 #to count the number of special charecters
digit_count=0 #to count the number of digits
length=len(passwrd) 
if(len(passwrd)>=8): #checking if the length of the password is greater than 8
    for index in range(0,len(passwrd)):
        if (passwrd[index].isdigit()): #incrementing digit_count if digit is present
            digit_count+=1
        elif (passwrd[index].isalpha()):#incrementing alpha_count if alphabet is present
            alpha_count+=1
        elif any(char in SpecialSym for char in passwrd):#incrementing splchar_count if special charecter is present
            splchar_count+=1
    if((digit_count>=1 and alpha_count>=1 and splchar_count>=1) and length>=16): #printing the level of password according to given conditions
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