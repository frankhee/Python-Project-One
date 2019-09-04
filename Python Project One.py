from IPython.display import clear_output
import random

def createBoard (board):
    clear_output()
    
    print("|"+ board[9]+"|"+ board[8] + "|"+ board[7] + "|")
    print("|"+ board[6]+"|"+ board[5] + "|"+ board[4] + "|")
    print("|"+ board[3]+"|"+ board[2] + "|"+ board[1] + "|")

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def placeMarker(board, marker, position):
    
    board[position] = marker

def winCheck(board,mark):
    return ((board[9] == mark and board[8] == mark and board[7] == mark)or
           (board[6] == mark and board[5] == mark and board[4] == mark)or
           (board[3] == mark and board[2] == mark and board[1] == mark)or
           (board[9] == mark and board[5] == mark and board[1] == mark)or
           (board[9] == mark and board[6] == mark and board[3] == mark)or
           (board[8] == mark and board[5] == mark and board[2] == mark)or
           (board[7] == mark and board[4] == mark and board[1] == mark)or
           (board[7] == mark and board [5] == mark and board[3] == mark))

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def validSpace(board,position):
    return board[position] == ' '

def fullBoardCheck(board):
    for i in range (1,10):
        if validSpace(board,i):
            return False
    return True

def playerPick (board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not validSpace(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    return input("Do you want to play again?").lower().startswith('y')
    

print("Welcome to Tic Tac Toe!")

while True:
    theBoard = [" "]* 10
    playOne, playTwo = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == "Player 1":
            createBoard(theBoard)
            position = playerPick(theBoard)
            placeMarker(theBoard,playOne,position)

            if winCheck(theBoard,playOne):
                createBoard(theBoard)
                print ("Congrats you won!")
                game_on = False
            else:
                if fullBoardCheck(theBoard):
                    createBoard(theBoard)
                    print("Game is a draw")
                    break
                else:
                    turn = "Player 2"
        else:
            createBoard(theBoard)
            position = playerPick(theBoard)
            placeMarker(theBoard,playTwo,position)

            if winCheck(theBoard,playTwo):
                createBoard(theBoard)
                print ("Congrats you won!")
                game_on = False
            else:
                if fullBoardCheck(theBoard):
                    createBoard(theBoard)
                    print("Game is a draw")
                    break
                else:
                    turn = "Player 1"
    if not replay():
        break

