budget=int(input("Enter your budget:")) #getiing budget from the user
city=input("Enter your city:")  #getiing city from the user
total=0
for i in range(100):    #calculating cost acoording to the city
    if(city=="chennai"):
        total+=40.5
    elif(city=="trichy"):
        total+=37.5
    elif(city=="madurai"):
        total+=44.5
    if(total>budget):
        print(i,"kgs of onion and tomato can be brought")
        break

