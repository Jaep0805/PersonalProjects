#board
#display board (using 2d array)
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
board = [['_','_','_','_','_','_','_'],
         ['_','_','_','_','_','_','_'],
         ['_','_','_','_','_','_','_'],
         ['_','_','_','_','_','_','_'],
         ['_','_','_','_','_','_','_'],
         ['_','_','_','_','_','_','_']] 


win = False
mode = ''
randarr = []

def displayBoard():
    #print index labels
    print(' ')
    print(' ', end = '')
    for num in range(1, 8):
        print(num, end = ' ')
    print('')    
    #makes a board of 6x7
    for x in range(0,6):
        print('|', end = '')
        for y in range(0,7):
            print(board[x][y] + '|', end = '')
        print('')


def handleTurn(player):
    if(player == 'Player1' or player == 'Player2'):
        position = 0
        while(position < 1 or position > 7):
            position = int(input(player + ", choose a position from 1 ~ 7 : "))
        indx = position - 1
        if not checkFull(indx):
            for val in range(5,-1, -1):
                if (board[val][indx] == '_'):
                    place(player, val, indx)
                    break      
        else :         
            print('You cannot place there, please choose a different position')
            handleTurn(player)
    elif(player == 'Computer'):
        randarr = []
        for i in range(0,7):
            if(not checkFull(i)):
                randarr.append(i)
            else:
                continue
        indx = int(random.choice(randarr))
        for val in range(5,-1, -1):
                if (board[val][indx] == '_'):
                    place(player, val, indx)
                    break  
        randarr.clear()

def checkFull(indx):
    #check board index
    for val in range(5,-1, -1):
        if (board[val][indx] == '_'):
            return False
    return True


def place(player, val, indx):
    #place O for player 1 and X for player 2
    if(player == 'Player1'):
        board[val][indx] = 'O'
    elif(player == 'Player2' or player == 'Computer'):
        board[val][indx] = 'X' 
        
    #display the updated board after every turn    
    displayBoard()


def checkwin():
    for x in range(0,6):
        for y in range(0,7):
            if(board[x][y] != '_'):
                #check vertical, horizontal and diagonal
                if(checklinear(x,y, 1, 0) or checklinear(x,y, 0, 1) or checklinear(x,y, 1, -1) or checklinear(x,y, 1, 1)):
                    return True
                else :
                    continue
            
   
def checklinear(x, y, stepX, stepY):
    startval = board[x][y]
    for i in range(0,4):
        try:
            if (board[abs(x + i * stepX)][abs(y + i * stepY)] != startval):
                return False
        except IndexError:
            return False
    
    return True

def checkBoardFull():
    for y in range(0,7):
        for x in range(0,6):
            if board[x][y] == '_':
                return False
    print('full')
    return True

def playGame(mode):
    displayBoard()
    player = mode
    #while win condition has not been satsified, play on
    while (not checkwin() and not checkBoardFull()):
        if(player == 'Player1'):
            player = mode
        elif(player == mode):
            player = 'Player1'   
        handleTurn(player)
    #since win condition as been satisfied, check if it is a tie, or a win
    if(checkwin()):
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
        playGame('Player2')
    elif(mode == 'computer'):
        print('////////')
        print('Computer mode')
        playGame('Computer')
    else:
        print('//////////////////////////')
        print('Please insert correct mode')
        play()

play()
# displayBoard()