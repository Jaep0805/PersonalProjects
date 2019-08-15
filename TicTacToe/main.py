#board
#display board
#turn
#play game
#check win
    #check rows
    #check columns
    #check diagonal
#check tie
#flip player
#ai implementation
import random

board = ['-','-','-',
         '-','-','-',
         '-','-','-']

win = False
mode = ''
randarr = []

def displayBoard():
    #makes a board of 3x3
    print(board[0] + '|' + board[1] + "|" + board[2])
    print(board[3] + '|' + board[4] + "|" + board[5])
    print(board[6] + '|' + board[7] + "|" + board[8])


def handleTurn(player):
    if(player == 'Player1' or player == 'Player2'):
        position = int(input(player + ", choose a position from 1 ~ 9 : "))
    elif(player == 'Computer'):
        for i in range(0,9):
            if board[i] == '-':
                randarr.append(i + 1)
            else:
                continue
        print(randarr)
        position = int(random.choice(randarr))
        randarr.clear()
        print(position)
    #check if location is already occupied
    while not board[position-1] == '-':
        print('you cannot place there')
        handleTurn(player)
    place(player, position)
    return


def place(player, position):
    #place O for player 1 and X for player 2
    if(player == 'Player1'):
        board[position-1] = 'O'
    elif(player == 'Player2' or player == 'Computer'):
        board[position-1] = 'X' 
        
    #display the updated board after every turn    
    displayBoard()


def checkwin():
    #horizontal and vertical
    if ((board[0] == 'O')&(board[1] == 'O')&(board[2] == 'O')):
        return True
    elif ((board[0] == 'X')&(board[1] == 'X')&(board[2] == 'X')):
        return True
    elif ((board[0] == 'O')&(board[3] == 'O')&(board[6] == 'O')):
        return True
    elif ((board[0] == 'X')&(board[3] == 'X')&(board[6] == 'X')):
        return True
    elif ((board[2] == 'O')&(board[5] == 'O')&(board[8] == 'O')):
        return True
    elif ((board[2] == 'X')&(board[5] == 'X')&(board[8] == 'X')):
        return True 
    elif ((board[6] == 'O')&(board[7] == 'O')&(board[8] == 'O')):
        return True 
    elif ((board[6] == 'X')&(board[7] == 'X')&(board[8] == 'X')):
        return True
    elif ((board[1] == 'O')&(board[4] == 'O')&(board[7] == 'O')):
        return True 
    elif ((board[1] == 'X')&(board[4] == 'X')&(board[7] == 'X')):
        return True
    elif ((board[3] == 'O')&(board[4] == 'O')&(board[5] == 'O')):
        return True 
    elif ((board[3] == 'X')&(board[4] == 'X')&(board[5] == 'X')):
        return True
    #diagonal
    elif ((board[0] == 'O')&(board[4] == 'O')&(board[8] == 'O')):
        return True 
    elif ((board[0] == 'X')&(board[4] == 'X')&(board[8] == 'X')):
        return True  
    elif ((board[2] == 'O')&(board[4] == 'O')&(board[6] == 'O')):
        return True 
    elif ((board[2] == 'X')&(board[4] == 'X')&(board[6] == 'X')):
        return True 
    else:
        return False

def checkfull():
    #check if the board is full and have not satisfied win condition
    for i in range(9):
        if board[i] == '-':
            return False
    return True


def pvp():
    displayBoard()
    player = 'Player2'
    #while win condition has not been satsified, play on
    while ((checkwin() == False) & (not checkfull())):
        if(player == 'Player1'):
            player = 'Player2'
        elif(player == 'Player2'):
            player = 'Player1'   
        handleTurn(player)
    #since win condition as been satisfied, check if it is a tie, or a win
    if(not checkfull() & checkwin()):
        #check that its not a tie, and someone has won
        print('///////////////////////')
        print(player + ' is the winner')
        print('///////////////////////')
    else:
        #else it is a tie
        print('///////////////////////')
        print('You have tied')
        print('///////////////////////')

def computer():
    displayBoard()
    player = 'Computer'
    while ((checkwin() == False) & (not checkfull())):
        if(player == 'Player1'):
            player = 'Computer'
        elif(player == 'Computer'):
            player = 'Player1'   
        handleTurn(player)
    if(not checkfull() & checkwin()):
        #check that its not a tie, and someone has won
        print('///////////////////////')
        print(player + ' is the winner')
        print('///////////////////////')
    else:
        #else it is a tie
        print('///////////////////////')
        print('You have tied')
        print('///////////////////////')

def play():
    print('Please choose a mode')
    mode = input('    pvp    OR   computer : ')
    if(mode == 'pvp'):
        print('////////')
        print('PvP mode')
        pvp()
    elif(mode == 'computer'):
        print('////////')
        print('Computer mode')
        computer()
    else:
        print('//////////////////////////')
        print('Please insert correct mode')
        play()

play()