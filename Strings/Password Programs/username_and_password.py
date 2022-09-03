'''Check if the username and password is correct. 
Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
name of the company mentioned in the username, followed by any 3 numbers.
eg username : myname@sayur.com. password - mnamesay123 '''

username=input("Enter the username:")
password=input("Enter the password:")
new_username=username.split('@')#spilting username after @
if(new_username[1].__contains__(".")):#spliting username after '.'
    new_username_1=new_username[1].split('.')
else:
    print("Username Invalid")
    exit()
if ((new_username_1[1]=="com") or (new_username_1[1]=="tech") or (new_username_1[1]=="edu") or (new_username_1[1]=="org")):#checking if username is valid
    print("Valid Username")
#checking if password is valid
if((password[0]==username[0] and password[1]==username[2]) and (password[2:5]==new_username[0][len(new_username[0])-3:len(new_username[0])]) and (password[5:8]==new_username_1[0][0:3]) and (password[8:11].isnumeric())):
    print("Valid Password")
else:
    print("Invalid Password")

'''Output:
Enter the username:myname@sayur.com
Enter the password:mnamesay123
com
Valid Username
Valid Password
'''
'''Enter the username:magavigna@gmail.com
Enter the password:maga
Valid Username
Invalid Password'''
'''Enter the username:magavigna@gmailcom
Enter the password:maga
Username Invalid'''