#coding:utf-8
#
board=["-","-","-",
        "-","-","-",
        "-","-","-"]

def display_board():
    print(board[0]+ "|" + board[1]+"|"+board[2])
    print(board[3]+ "|" + board[4]+"|"+board[5])
    print(board[6]+ "|" + board[7]+"|"+board[8])

def play_game():
    
    
    
    #Display_board

    display_board()    



    handle_turn()



def handle_turn():
    position = input("Choose a position from 1-9:")
    position = int(position) - 1

    board[position] = "X"
    display_board()



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