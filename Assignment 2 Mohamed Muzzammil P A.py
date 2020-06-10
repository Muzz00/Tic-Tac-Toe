#Mohamed Muzzamil P A (1519805)
#Programming Fundamentals Assignment 2


#FUNCTIONS

#Default settigs
def default():
    global game
    global player1
    global player2
    global run_game
    global winner
    game = ["   ", "   ", "   ",
            "   ", "   ", "   ",
            "   ", "   ", "   "]

    player1 = ""
    player2 = ""
    run_game = True
    winner = ""

#Asking the user if the want to be X or O
def player_x_o():
    global player1
    global player2
    global current_player
    player1 = ""
    while player1 not in ["X","O"]:
        player1 = input("Would you like to be X or O: ")
        player1 = player1.upper().strip()
    player1 = " " + player1 +  " "

    if player1 == " X ":
        player2 = " O "
    elif player1 == " O ":
        player2 = " X "
    current_player = player1
    print("\n")


#Displays Game
def display_game():
    print("\n")
    print("    Columns")
    print(" 1 "+ "   " + " 2 " + "   " + " 3 \n")
    print(game[0] + " | " + game[1] + " | " + game[2] + "   1")
    print("---" + " + " + "---" + " + " + "---")
    print(game[3] + " | " + game[4] + " | " + game[5] + "   2   Rows")
    print("---" + " + " + "---" + " + " + "---")
    print(game[6] + " | " + game[7] + " | " + game[8] + "   3")
    print("\n")

#Swap Players from X to O and O to X
def swap_player():
    global current_player
    if current_player == player1:
        current_player = player2
    elif current_player == player2:
        current_player = player1

#Converting row and columns into index
def get_index(row,col):
    if row == 1 and col == 1:
        ind = 0
        
    elif row == 1 and col == 2:
        ind = 1
        
    elif row == 1 and col == 3:
        ind = 2
        
    elif row == 2 and col == 1:
        ind = 3

    elif row == 2 and col == 2:
        ind = 4

    elif row == 2 and col == 3:
        ind = 5

    elif row == 3 and col == 1:
        ind = 6

    elif row == 3 and col == 2:
        ind = 7

    elif row == 3 and col == 3:
        ind = 8

    return ind

#Rules for Rows
def row_rule():
    global run_game
    row1 = game[0] == game[1] == game[2] != "   "
    row2 = game[3] == game[4] == game[5] != "   "
    row3 = game[6] == game[7] == game[8] != "   "

    if row1 or row2 or row3:
        run_game = False

    if row1:
        return game[0]

    elif row2:
        return game[3]

    elif row3:
        return game[6]

    else:
        return None

#Rules for the Coloumns
def col_rule():
    global run_game
    col1 = game[0] == game[3] == game[6] != "   "
    col2 = game[1] == game[4] == game[7] != "   "
    col3 = game[2] == game[5] == game[8] != "   "

    if col1 or col2 or col3:
        run_game = False

    if col1:
        return game[0]

    elif col2:
        return game[1]

    elif col3:
        return game[2]

    else:
        return None

#Rules for Diagnols
def diag_rule():
    global run_game
    diag1 = game[0] == game[4] == game[8] != "   "
    diag2 = game[2] == game[4] == game[6] != "   "

    if diag1 or diag2:
        run_game = False

    if diag1:
        return game[0]

    elif diag2:
        return game[2]

    else:
        return None

#Determining if ther is a winner
def winner_is():
    global winner

    row_winner = row_rule()
    col_winner = col_rule()
    diag_winner = diag_rule()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None

#Checking for Winner or Tie
def win_tie():
    winner_is()
    global winner
    if "   " not in game and winner == None:
        winner = "Tie"




#Game Code starts from here
stop = ""
while stop != "q":
    default()
    player_x_o()

    
    while "   " in game and run_game:
        display_game()
        row = int(input("\nPlease select a row: "))
        while row < 1 or row > 3:
            row = int(input("You entered a invalid row please select a row from 1-3: "))
        col = int(input("Please select a column: "))
        while col < 1 or col > 3:
            col = int(input("You entered a invalid row please select a row from 1-3: "))


        index = get_index(row,col)

        while game[index] == " X " or game[index] == " O ":
            print("\n\nThere is already a X or O Please go again")
            display_game()
            row = int(input("Please select a row: "))
            while row < 1 or row > 3:
                row = int(input("You entered a invalid row please select a row from 1-3: "))
            col = int(input("Please select a column: "))
            while col < 1 or col > 3:
                col = int(input("You entered a invalid row please select a row from 1-3: "))

            index = get_index(row,col)


        game.insert(index,current_player)
        del game[index+1]

        win_tie()

        if winner == player1 or winner == player2:
            display_game()
            print("\n\nThe winner for this game was" + winner)
        elif winner == "Tie":
            display_game()
            print("\n\nIt's a tie")



        swap_player()
        
    stop = input("Please press q to quit the game or press enter to play again: ")
    



print("\nYou have quit the game, Thanks for playing! :)")
