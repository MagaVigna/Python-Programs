word=input("Enter any string:") #getting the input string
new_word=[] #to store the string with replaced letters
replace=input("Enter the letter to be replaced:")
replace_word=input("Enter the letter to be replaced with:")
for index in range(0,len(word)):
    if word[index]==replace: #if entered char is same as the char in the string appending the letter that needs to replace in the new string
        new_word.append(replace_word)
    else: #else replacing char in the original string
        new_word.append(word[index])
print("Old string:",*word)
print("New string:",*new_word)

'''Output:
Enter any string:applw
Enter the letter to be replaced:w
Enter the letter to be replaced with:e
Old string: a p p l w
New string: a p p l e'''
'''Enter any string:hello
Enter the letter to be replaced:l
Enter the letter to be replaced with:o
Old string: h e l l o
New string: h e o o o'''