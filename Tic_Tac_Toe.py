 
board=["_", "_", "_", "_", "_", "_", "_", "_", "_"]

current_player="X"
win=None
game_continue=True
turn=0

# function to print board

def print_board():
    print(board[0]+ " | "+ board[1]+" | " + board[2])
    print(board[3]+ " | "+ board[4]+" | " + board[5])
    print(board[6]+ " | "+ board[7]+" | " + board[8])

# funtion to take input position and enter it in the board

def input_position():

    global turn
    global current_player
    check=False

    print(current_player + "turn's \n")

    while not check:

     pos=int(input("enter the position : "))
     pos=pos-1

     if pos>9 or pos<0 :
        print("invalid position enter a valid position \n\n")

     if board[pos]=="_":
        check=True
     else:
        print("position already filled....enter any other position")

    board[pos]=current_player
    turn=turn+1

# funtion to flip the player after every turn

def flip_turn():

 global current_player
 
 if current_player=="X":
  current_player="0"
 else:
  current_player="X"
 
# function to check who win or tie after every turn

def check_for_win():

    global game_continue
    
    if  board[0]==board[1]==board[2] !="_" or board[3]==board[4]==board[5] !="_" or board[6]==board[7]==board[8] !="_" :

     game_continue=False

     return current_player
        
    elif  board[0]==board[3]==board[6] !="_" or board[1]==board[4]==board[7] !="_" or board[5]==board[2]==board[8] !="_" :

        game_continue=False
        return current_player
        
    elif  board[0]==board[8]==board[4] !="_" or board[6]==board[4]==board[2] !="_"  :

        game_continue=False

        return current_player


    if turn==9:
        game_continue=False
        return None
 


current_player=input("Enter first player : ")

while (game_continue):

 print_board()
 input_position()
 win=check_for_win()
 flip_turn()
 
if win==None:
    print("Tie game")
else:
 print(win + " won the game")





