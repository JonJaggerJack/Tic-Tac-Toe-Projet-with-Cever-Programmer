#coding:utf-8
#global variables

board=["-","-","-",
        "-","-","-",
        "-","-","-"]
#If game still is going

game_still_going = True


#whole won?or tie?
winner = None
#Whos turn is it
current_player ="X"

def display_board():
    print(board[0]+ "|" + board[1]+"|"+board[2])
    print(board[3]+ "|" + board[4]+"|"+board[5])
    print(board[6]+ "|" + board[7]+"|"+board[8])

def play_game():
    
    #Display_board

    display_board()    

    while game_still_going:
        #handle a single turn of an arbitrary player
        handle_turn(current_player)
    #check if the game has ended
        check_if_game_over()
        #Flip to the other player
        flip_player()

   #The game has ended

   if winner == "X" or winner == "O"
        print(winner + "won.")
    elif winner == None:
        print("Tie.")   
     

def handle_turn(player):
    position = input("Choose a position from 1-9:")
    position = int(position) - 1

    board[position] = "X"

    display_board()


def check_if_game_over():
    check_for_winner()
    checkif_tie()

def check_for_winner():
    global winner

    row_winner = check_rows()

    colums_winner = check_columns()

    diagonal_winner = check_diagonals()
    if row_winner:
    elif column_winner:
        winner=columns_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
      winner = None  
    return

def check_rows():
    return

def check_colums():
    return

def check_diagonals():
    return

def check_if_tie():
    return

def flip_player():
    return


play_game()


#board

#display


#play game 


#handle win



#check win
    #check rows
    #check colums
    #check diagonals





#check tie


#flip player
