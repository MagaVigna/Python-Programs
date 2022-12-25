built_in_word=[]
built_in_word_1=["d","o","t"] #declaring the words that to should be guessed by the user
built_in_word_2=["w","a","l","k"]
built_in_word_3=["h","e","l","l","o"]


def get_input(): #function to get the input from the user
    global input_word
    input_word_as_string=input("Enter the word:")
    input_word=list(input_word_as_string) #converting the string into a list of charecters

def fixing_the_built_in_word(word):#declaring the words for the user to guess according to the length
    global built_in_word
    if len(word)==3: #if the length of word is three then the word user has to guess is fixed with the same length word
        built_in_word=built_in_word_1.copy()
    elif len(word)==4: #if the length of word is four then the word user has to guess is fixed with the four length word
        built_in_word=built_in_word_2.copy()
    elif len(word)==5: #if the length of word is five then the word user has to guess is fixed with the five length word
        built_in_word=built_in_word_3.copy()

def check_word(word): #checking if the user entered word is correct or wrong
    global found_letter
    found_letter=[] #a list to store the charecters that occur both in user input word and the built in word
    for index in range (0,len(word)): #to manipulate the string
        if built_in_word[index]==word[index]: #if letter found in the given string printing G
            print(word[index],"- G")
            # found at the wrond position printing Y
            found_letter.append(word[index])
        elif word[index] in built_in_word:
            if word.count(word[index])>built_in_word.count(word[index]): 
                print(word[index],"- R")
                word[index]="@"
            elif word.count(word[index])==built_in_word.count(word[index]):
                print(word[index],"- Y")
        else:   #not found at all printing R
            print(word[index],"- R")

def wordle_main():
    global next_round
    next_round=1
    level=3
    if next_round==1: #checking if the user passes the round to move on to the next round
        while level<=5: #to play levels from three to five
            for attempt in range (0,5):
                print("-----Guess the", level , "letter word------")
                get_input() #getting the input
                if level!=len(input_word):
                    print("Please enter a",level,"letter word")
                    break
                fixing_the_built_in_word(input_word) #deciding the word to be guessed by the user
                check_word(input_word) #checking the word
                if input_word==found_letter: 
                    next_round=0
                    level=level+1
                    built_in_word.clear()
                    break
                if attempt==4:
                    level=6

        
wordle_main()

'''
Output:
-----Guess the 3 letter word------
Enter the word:dot
d - G
o - G
t - G
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
'''
-----Guess the 3 letter word------
Enter the word:ooo
o - R
o - G
o - R
-----Guess the 3 letter word------
Enter the word:ddd
d - G
d - R
d - R
-----Guess the 3 letter word------
Enter the word:ttt
t - R
t - R
t - G
-----Guess the 3 letter word------
Enter the word:dot
d - G
o - G
t - G
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
'''
-----Guess the 3 letter word------
Enter the word:ooo
o - R
o - G
o - R
-----Guess the 3 letter word------
Enter the word:lll
l - R
l - R
l - R
-----Guess the 3 letter word------
Enter the word:kkk
k - R
k - R
k - R
-----Guess the 3 letter word------
Enter the word:mmm
m - R
m - R
m - R
-----Guess the 3 letter word------
Enter the word:nnn
n - R
n - R
n - R
'''