'''
You have a message that you want to send to your friend. You don't want others to see the message. You code the message and send it.
The alg to code is - split each word in half and reverse it (eg cricket becomes ketccri), if the word ends with a vowel, split at the 
last letter and reverse (eg cinema becomes acinem), if the word has numbers, spell the number but add A as first and last letters
(8 pm becomes AeightA pm ).
Write an app that can code and decode the message.
'''
message="meet me at 8 pm" #hardcoding the message value
message_list=message.split(" ") #converting the string into list
vowels="aeiou" #declaring the vowel values

def encoding(word): #function to split the word into half and reverse it
    global first_half, second_half, encoded_word
    first_half=word[:len(word)//2]
    second_half=word[len(word)//2:]
    encoded_word=second_half+first_half
    print(encoded_word)

def encoding_words_with_vowels(word): #function to spilt the last letter and reverse it if the last letter is a vowel
    global first_half, second_half, encoded_word
    first_half=word[len(word)]
    second_half=word[:len(word)-1]
    encoded_word=second_half+first_half
    print(encoded_word)

def encoding_words_with_numbers(word): #finction to spell the number and add A in first and last position if the message has number present in it

    global number
    dictionary = { 0:"zero" , 1:"one" , 2:"two" , 3:"three" , 4:"four" , 5:"five" , 6:"six" ,7:"seven" , 8:"eight" , 9:"nine"} #storing the integer in key part of dictionary and english word of it in value part of dictionary
    number = [int(element) for element in word.split() if element.isdigit()]
    for num in number : #printing the corresponding english word for the number
        print("A"+dictionary[num]+"A")

for charecter in message_list: #calling the functions accordingly
    if charecter.isdigit():
        encoding_words_with_numbers(charecter)
    
    elif message_list[len(message_list)-1] in vowels:
        encoding_words_with_vowels(message_list[len(message_list)-1])

    else:
        encoding(charecter)

'''
Output:
etme
em
ta
AeightA
mp
'''
