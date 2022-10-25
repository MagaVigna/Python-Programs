'''
Write an app for the follwoing two player game. You have a 6 x 6 board. 
Users take turns rolling the dice twice. first roll is row no, second roll is col number. Mark the spot (row, col) as claimed by the user
who rolled the dice.
When the user rolls the dice within 1 col/row of a claimed spot of the other user, the other user gets a point. 
If the spot is same as the claimed spot of the other user, the user that rolled the dice gets a point. 
The player who gets 5 points first wins the game.
'''

import random
board=[[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]
player1_points=0
player2_points=0
turns=1

def fixing_row_col(): #function to declare the row and column player 1 and 2 according to their dice value
    global player1_row,player1_col,player2_row,player2_col,turns,board
    while (player1_points<5) and (player2_points<5):
        print("Player one chance to roll the dice") #player 1 rolling the dice
        player1_row=random.randint(0,5) #player 1 row
        player1_col=random.randint(0,5) #player 1 column
        printing_the_row_col(player1_row,player1_col) #printing player 1 row and column values
        board[player1_row][player1_col]=1 #changing the player1_row x player1_col value to 1 
        printing_the_board() #printing the contents in the board
        print("Player two chance to roll the dice") #player 2 rolling the dice
        player2_row=random.randint(0,5) #player 2 row
        player2_col=random.randint(0,5) #player 2 column
        printing_the_row_col(player2_row,player2_col) #printing player 2 row and column values
        board[player2_row][player2_col]=2 #changing the player2_row x player2_col value to 2
        printing_the_board() #printing the contents in the board
        declaring_points(player1_row,player1_col,turns) #function to decide player 1 points
        turns=turns+1
        declaring_points(player2_row,player2_col,turns) #function to decide player 2 points
        turns=turns+1
        

def printing_the_row_col(row,col): #function to print the row and column the player got while rolling the dice
    print("The row value player got is:",row+1)
    print("The column value the player got is:",col+1)

def printing_the_board(): #function to print the values in the board list
    for row_value in board:
        for col_value in row_value:
            print(col_value,end=" ")
        print()

def declaring_points(row,col,turn): #function to find out who got the point 
    global player1_points,player2_points
    try:
        if player1_row==player2_row and player1_col==player2_col:
            if turn%2==0:
                player2_points=player2_points+1
            else:
                player1_points=player1_points+1
        elif ((board[row+1][col]!=0) or (board[row-1][col]!=0) or  (board[row][col+1]!=0) or (board[row][col-1]!=0) or (board[row-1][col-1]!=0) or (board[row+1][col+1]!=0) or (board[row+1][col-1]!=0) or (board[row-1][col+1]!=0) or (board[row+1][col-1]!=0)):
            if turn%2==0:
                player2_points=player2_points+1
            else:
                player1_points=player1_points+1
    except IndexError:
        pass
    
    
fixing_row_col()
print("Points scored by player 1 is:",player1_points)
print("Points scored by player 2 is:",player2_points)

'''
Output:
Player one chance to roll the dice
The row value player got is: 3
The column value the player got is: 2
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 4
The column value the player got is: 3
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 0 0 0
0 0 2 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 3
The column value the player got is: 4
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 1 0 0
0 0 2 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 3
The column value the player got is: 6
0 0 0 0 0 0
0 0 0 0 0 0
0 1 0 1 0 2
0 0 2 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 3
The column value the player got is: 1
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 1 0 2
0 0 2 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 3
The column value the player got is: 5
0 0 0 0 0 0 
0 0 0 0 0 0
1 1 0 1 2 2
0 0 2 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 3
The column value the player got is: 5
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 1 1 2
0 0 2 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 5
The column value the player got is: 6
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 1 1 2
0 0 2 0 0 0
0 0 0 0 0 2
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 6
The column value the player got is: 4
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 1 1 2
0 0 2 0 0 0
0 0 0 0 0 2
0 0 0 1 0 0
Player two chance to roll the dice
The row value player got is: 5
The column value the player got is: 6
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 1 1 2
0 0 2 0 0 0
0 0 0 0 0 2
0 0 0 1 0 0
Player one chance to roll the dice
The row value player got is: 5
The column value the player got is: 4
0 0 0 0 0 0
0 0 0 0 0 0
1 1 0 1 1 2
0 0 2 0 0 0
0 0 0 1 0 2
0 0 0 1 0 0
Player two chance to roll the dice
The row value player got is: 2
The column value the player got is: 4
0 0 0 0 0 0
0 0 0 2 0 0
1 1 0 1 1 2
0 0 2 0 0 0
0 0 0 1 0 2
0 0 0 1 0 0
Points scored by player 1 is: 5
Points scored by player 2 is: 3
'''
'''
Player one chance to roll the dice
The row value player got is: 5
The column value the player got is: 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 1
The column value the player got is: 5
0 0 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 1
The column value the player got is: 6
0 0 0 0 2 1
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 3
The column value the player got is: 6
0 0 0 0 2 1
0 0 0 0 0 0
0 0 0 0 0 2
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 2
The column value the player got is: 2
0 0 0 0 2 1
0 1 0 0 0 0
0 0 0 0 0 2
0 0 0 0 0 0 
0 0 0 0 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 1
The column value the player got is: 2
0 2 0 0 2 1
0 1 0 0 0 0
0 0 0 0 0 2
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 3
The column value the player got is: 4
0 2 0 0 2 1
0 1 0 0 0 0
0 0 0 1 0 2
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 1
The column value the player got is: 6
0 2 0 0 2 2
0 1 0 0 0 0
0 0 0 1 0 2
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 3
The column value the player got is: 3
0 2 0 0 2 2
0 1 0 0 0 0
0 0 1 1 0 2
0 0 0 0 0 0
0 0 0 0 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 5
The column value the player got is: 4
0 2 0 0 2 2
0 1 0 0 0 0
0 0 1 1 0 2
0 0 0 0 0 0
0 0 0 2 0 1
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 2
The column value the player got is: 6
0 2 0 0 2 2
0 1 0 0 0 1
0 0 1 1 0 2
0 0 0 0 0 0
0 0 0 2 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 1
The column value the player got is: 4
0 2 0 2 2 2
0 1 0 0 0 1
0 0 1 1 0 2
0 0 0 0 0 0
0 0 0 2 0 1
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 5
The column value the player got is: 2
0 2 0 2 2 2
0 1 0 0 0 1
0 0 1 1 0 2
0 0 0 0 0 0
0 1 0 2 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 4
The column value the player got is: 4
0 2 0 2 2 2
0 1 0 0 0 1
0 0 1 1 0 2
0 0 0 2 0 0
0 1 0 2 0 1
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 3
The column value the player got is: 4
0 2 0 2 2 2
0 1 0 0 0 1
0 0 1 1 0 2
0 0 0 2 0 0
0 1 0 2 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 2
The column value the player got is: 5
0 2 0 2 2 2
0 1 0 0 2 1
0 0 1 1 0 2
0 0 0 2 0 0
0 1 0 2 0 1
0 0 0 0 0 0
Player one chance to roll the dice
The row value player got is: 4
The column value the player got is: 4
0 2 0 2 2 2
0 1 0 0 2 1
0 0 1 1 0 2
0 0 0 1 0 0
0 1 0 2 0 1
0 0 0 0 0 0
Player two chance to roll the dice
The row value player got is: 4
The column value the player got is: 4
0 2 0 2 2 2
0 1 0 0 2 1
0 0 1 1 0 2
0 0 0 2 0 0
0 1 0 2 0 1
0 0 0 0 0 0
Points scored by player 1 is: 5
Points scored by player 2 is: 5
'''