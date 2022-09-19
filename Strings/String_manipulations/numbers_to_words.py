number = input ("Enter a number:") #getting an number from the user
dictionary = { "0":"zero" , "1":"one" , "2":"two" , "3":"three" , "4":"four" , "5":"five" , "6":"six" ,
 "7":"seven" , "8":"eight" , "9":"nine"} #storing the integer in key part of dictionary and english word of it in value part of dictionary
for num in number : #printing the corresponding english word for the number 
      print(dictionary[num], end = " ")

'''Output:
Enter a number:10
one zero '''