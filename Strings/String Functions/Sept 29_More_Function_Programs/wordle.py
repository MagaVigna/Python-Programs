'''
6. Code the game Wordle (text based. Instead of color, use letters - G for green, Y for yellow and B for grey). 
https://www.nytimes.com/games/wordle/index.html
Start with 3 letter word. If user guesses the word correctly, then 4 letters and then 5 letters. 
'''

three_letter_word="dot" #declaring the words that to should be guessed by the user
four_letter_word="play"
five_letter_word="excel"


def get_input(): #function to get the input from the user
    global input_word
    input_word=input("Enter the word:")

def wordle_function(word):
    global found_letter
    found_letter=[]
    if len(word)==3: #decalring the words according to the length
        built_in_word=three_letter_word
    elif len(word)==4:
        built_in_word=four_letter_word
    elif len(word)==5:
        built_in_word=five_letter_word
    for index in range (0,len(word)): #to manipulate the string
        if built_in_word[index]==input_word[index]: #if letter founf in the given string printing G
            print(input_word[index],"- G")
            found_letter.append(input_word[index])#found at the wrond position printing Y
        elif input_word[index] in built_in_word:
            print(input_word[index],"- Y")
        else:   #not found at all printing B
            print(input_word[index],"- B")

def wordle_main():
    global next_round
    next_round=0
    for attempt in range (0,5): #three letter word round
        print("-----Guess the three letter word------")
        get_input()
        word_list=string_to_list(input_word)
        wordle_function(input_word)
        if word_list==found_letter:
            next_round=1
            break

    for attempt in range (0,5): #four letter word round
        global third_round
        third_round=0
        if next_round:
            print("-----Guess the four letter word------")
            get_input()
            word_list=string_to_list(input_word)
            wordle_function(input_word)
            if word_list==found_letter:
                third_round=1
                break
            
    for attempt in range (1,5): #five letter word round
        if third_round:
            print("-----Guess the five letter word------")
            get_input()
            wordle_function(input_word)
            if word_list==found_letter:
                print("Thank you for playing")
                exit()
        else:
            exit()

def string_to_list(input_string): #converting the input string into list for comparing the string the stored string
    temp_word=[]
    temp_word[:0]=input_string
    return temp_word

wordle_main()

'''
Output:
-----Guess the three letter word------
Enter the word:dot
d - G
o - G
t - G
-----Guess the four letter word------
Enter the word:four
f - B
o - B
u - B
r - B
-----Guess the four letter word------
Enter the word:hell
h - B
e - Y
l - B
l - B
-----Guess the four letter word------
Enter the word:olay
o - B
l - G
a - G
y - G
-----Guess the four letter word------
Enter the word:play
p - G
l - G
a - G
y - G
-----Guess the five letter word------
Enter the word:hello
h - B
e - B
l - B
l - B
o - B
Thank you for playing'''