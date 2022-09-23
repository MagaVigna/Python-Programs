'''
calorie need calculator.
a function that calculates how much calorie a user should intake to maintain their current weight
Input: weight,height,age,gender,activity level
Output: total calorie needs
'''

activity_level_list=["sedentry","lightly active","mmoderately active","very active","extra active"] #declaring the activity levels

def user_details(): #function to get the details of the user
    global weight,height,age,user_activity_level,gender,activity_level_list
    weight=float(input("Enter your weight in kgs:"))
    height=float(input("Enter your height in cms:"))
    age=int(input("Enter your age in years:"))
    gender=input("Enter M for male and F for Female:")
    print("Choose your activity level:")
    for index in range(0,len(activity_level_list)): #printing the activity level lists
        print(index+1," - ",activity_level_list[index])
    user_activity_level=int(input())

def bmr_calculation(): #calculating bmr
    global bmr
    if gender=="F":    
        bmr=655+(9.6*weight)+(1.8*height)-(4.7*age) #calculating bmr for female according to harris_bennedict formula
    elif gender=="M":
        bmr=66+(13.7*weight)+(5*height)-(6.8*age) #calculating bmr for male according to harris_bennedict formula
    else:
        print("Enter the correct gender!!!")
        exit()

def calorie_needs_calculation(): #function to calculate calories need to maintain the users current weight
    global calories
    user_details()
    bmr_calculation()
    if user_activity_level==1:
        calories=bmr*1.2
    elif user_activity_level==2:
        calories=bmr*1.375
    elif user_activity_level==3:
        calories=bmr*1.55
    elif user_activity_level==4:
        calories=bmr*1.725
    elif user_activity_level==5:
        calories=bmr*1.9
    else:
        print("Choose the correct activity level from the list!!!")
        exit()

def calories_needs_print(): #printing the bmr and the calorie needs
    print("Your BMR is : ",bmr)
    print("In order to maintain your current weight, the total number of calories you need is:")
    print(int(calories))

calorie_needs_calculation()
calories_needs_print()

'''
Output:
Enter your weight in kgs:84
Enter your height in cms:162.5
Enter your age in years:32
Enter M for male and F for Female:F
Choose your activity level:
1  -  sedentry
2  -  lightly active
3  -  mmoderately active
4  -  very active
5  -  extra active
1
Your BMR is :  1603.5
In order to maintain your current weight, the total number of calories you need is:
1924
'''

'''
Enter your weight in kgs:50
Enter your height in cms:162
Enter your age in years:19
Enter M for male and F for Female:M
Choose your activity level:
1  -  sedentry
2  -  lightly active
3  -  mmoderately active
4  -  very active
5  -  extra active
2
Your BMR is :  1431.8
In order to maintain your current weight, the total number of calories you need is:
1968
'''
'''
Enter your weight in kgs:60
Enter your height in cms:170
Enter your age in years:30
Enter M for male and F for Female:g
Choose your activity level:
1  -  sedentry
2  -  lightly active
3  -  mmoderately active
4  -  very active
5  -  extra active
6
Enter the correct gender!!!
'''