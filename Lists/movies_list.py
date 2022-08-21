friends_list=[]
my_list=["Titanic","Harry Potter","Twilight","Inception"] #declaring movies I watched
both_watched=[]
no_of_movies=int(input("Enter the number of movies you have watched:"))

for movie in range(0,no_of_movies):
    
    temp=(input("Enter the movie name:"))
    friends_list.append(temp) #Getting friends movie list

for my_movie in range(0,len(my_list)):
    for movie in range(0,len(friends_list)):
        if(my_list[my_movie]==friends_list[movie]):
            both_watched.append(my_list[my_movie]) #Finding the movies we both watched
            my_list.pop(my_movie) #deleting the movies we both watched from both our lists
            friends_list.pop(movie)

print("Movies we both watched:") 
for movie in range(0,len(both_watched)):
    print(both_watched[movie])

print("Movies only I watched:")
for movie in range(0,len(my_list)):
    print(my_list[movie])

print("Movies only my friend watched:")
for movie in range(0,len(friends_list)):
    print(friends_list[movie])