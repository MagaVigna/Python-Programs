budget=int(input("Enter your budget:")) #getiing budget as input
total=0
for i in range(100):
    total+=30.5 #because onion=20 and toamto=10.5 
    if(total>budget):
        print(i,"kgs of onion and tomato can be brought")
        break

