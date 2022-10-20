built_in_word=[]
built_in_word_1=["d","o","t"] #declaring the words that to should be guessed by the user
built_in_word_2=["w","a","l","k"]
built_in_word_3=["s","a","y","u","r"]


def get_input(): #function to get the input from the user
    global input_word
    input_word_as_string=input("Enter the word:")
    input_word=list(input_word_as_string)

def fixing_the_built_in_word(word):
    for index in range (0,len(word)):
        if len(word)==3: #declaring the words according to the length
            built_in_word.append(built_in_word_1[index])
        elif len(word)==4:
            built_in_word.append(built_in_word_2[index])
        elif len(word)==5:
            built_in_word.append(built_in_word_3[index])

def check_word(word):
    global found_letter
    found_letter=[]
    for index in range (0,len(word)): #to manipulate the string
        if built_in_word[index]==word[index]: #if letter found in the given string printing G
            print(word[index],"- G")
            found_letter.append(word[index])#found at the wrond position printing Y
        elif word[index] in built_in_word:
            print(word[index],"- Y")
        else:   #not found at all printing B
            print(word[index],"- B")

def wordle_main():
    global next_round
    next_round=1
    level=3
    if next_round==1:
        while level<=5:
            for attempt in range (0,5):
                print("-----Guess the", level , "letter word------")
                get_input()
                fixing_the_built_in_word(input_word)
                check_word(input_word)
                if input_word==found_letter:
                    next_round=0
                    level=level+1
                    built_in_word.clear()
                    break
        
wordle_main()

'''
Output:
-----Guess the 3 letter word------
Enter the word:dot
d - G
o - G
t - G
-----Guess the 4 letter word------
Enter the word:well
w - G
e - B
l - G
l - Y
-----Guess the 4 letter word------
Enter the word:walk
w - G
a - G
l - G
k - G
-----Guess the 5 letter word------
Enter the word:sayur
s - G
a - G
y - G
u - G
r - G
'''