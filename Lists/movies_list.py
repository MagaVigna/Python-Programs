friends_list=[]
my_list=["Titanic","Harry Potter","Twilight","Inception"] #declaring movies I watched
both_watched=[]
no_of_movies=int(input("Enter the number of movies you have watched:"))

for movie in range(0,no_of_movies):
    
    temp=(input("Enter the movie name:"))
    friends_list.append(temp) #Getting friends movie list

for my_movie in my_list:
    if my_movie in friends_list:
            both_watched.append(my_movie) #Finding the movies we both watched
            my_list.remove(my_movie) #deleting the movies we both watched from both our lists
            friends_list.remove(my_movie)

print("Movies we both watched:") 
for movie in range(0,len(both_watched)):
    print(both_watched[movie])

print("Movies only I watched:")
for movie in range(0,len(my_list)):
    print(my_list[movie])

print("Movies only my friend watched:")
for movie in range(0,len(friends_list)):
    print(friends_list[movie])

'''Output:
Enter the number of movies you have watched:2
Enter the movie name:Twilight
Enter the movie name:After
Movies we both watched:
Twilight
Movies only I watched:
Titanic
Harry Potter
Inception
Movies only my friend watched:
After'''