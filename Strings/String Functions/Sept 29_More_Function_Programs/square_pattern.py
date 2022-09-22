'''
5. Write a function that displays a square box with '*'. Input is the width of the sqaure.
'''

def printing_star_square(width): #function to print the square
    for row in range(width): #loop for rows
        for column in range(width): #loop for columns
            if(row == 0 or row == width - 1 or column == 0 or column == width - 1): #checking if the row or column is the margin of the square 
                print('*', end = ' ') #if yes prinitng a star
            else:
                print(' ', end = ' ') #if no printing a blank space
        print()

width = int(input("Enter the side of the square  : ")) #getting width from the user
printing_star_square(width) #calling the function

'''
Output:
Enter the side of the square  : 5
* * * * * 
*       *
*       *
*       *
* * * * *
'''
'''
Enter the side of the square  : 2
* * 
* *
'''
'''
Enter the side of the square  : 10
* * * * * * * * * * 
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
*                 *
* * * * * * * * * *
'''