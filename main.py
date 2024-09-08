import os
import sys
import random

BOARD = []
COMPUTERSIGN = ""
PLAYERSIGN = ""

def playerTurn():
    clearTerminal()
    showBoard()

    playerAnswer = int()

    alowedAnswer = False

    while alowedAnswer == False:
        playerAnswer = int(input("Where would you like to go?"))
        
        if playerAnswer < 1:
            print("Number must be above 1")
        elif playerAnswer > 9:
            print("Number must be less than 9")
        elif playerAnswer - 1 not in getPossibleMoves(getBoard()):
            print("Spot taken")
        else:
            changeGlobalBoard(playerAnswer - 1, PLAYERSIGN)
            if checkWin(getBoard(), PLAYERSIGN):
                win(PLAYERSIGN)
            tie()
            computerTurn()

def computerTurn():
    board = getBoard()

    defendingMoves = getDefendingMoves(board)
    winningMoves = getWinningMoves(board)
    normalMoves = getNormalMoves(board)

    if len(winningMoves) != 0:
        changeGlobalBoard(random.choice(winningMoves), COMPUTERSIGN)
        win(COMPUTERSIGN)
    elif len(defendingMoves) != 0:
        changeGlobalBoard(random.choice(defendingMoves) , COMPUTERSIGN)
    else:
        changeGlobalBoard(random.choice(normalMoves), COMPUTERSIGN)
    
    tie()
    playerTurn()

def getWinningMoves(board):
    possibleMoves = getPossibleMoves(board)
    winningMoves = []

    for i in possibleMoves:
        board[i] = COMPUTERSIGN
        if checkWin(board, COMPUTERSIGN) == True:
            winningMoves.append(i)
        board[i] = " "
    return winningMoves

def getDefendingMoves(board):
    possibleMoves = getPossibleMoves(board)
    defendingMoves = []

    for i in possibleMoves:
        board[i] = PLAYERSIGN
        if checkWin(board, PLAYERSIGN) == True:
            defendingMoves.append(i)
        board[i] = " "
    return defendingMoves

def getNormalMoves(board):
    possibleMoves = getPossibleMoves(board)
    normalMoves = []

    winningMoves = getWinningMoves(board)
    defendingMoves = getDefendingMoves(board)

    for i in possibleMoves:
        if i not in winningMoves and i not in defendingMoves:
            normalMoves.append(i)
    return normalMoves

def getPossibleMoves(board):
    possibleMoves = []

    for i in range(len(board)):
        if board[i] == " ":
            possibleMoves.append(i)
    
    return possibleMoves

def clearTerminal():
    os.system("clear")

def getBoard():
    return BOARD.copy()

def showBoard():
    board = getBoard()

    print(board[0]+"|"+ board[1]+"|"+ board[2])
    print("-----")
    print(board[3]+"|"+ board[4]+"|"+ board[5])
    print("-----")
    print(board[6]+"|"+ board[7]+"|"+ board[8])

def checkWin(board, sign):
    #Horizontals
    if board[0] == sign and board[1] == sign and board[2] == sign:
        return True
    elif board[3] == sign and board[4] == sign and board[5] == sign:
        return True
    elif board[6] == sign and board[7] == sign and board[8] == sign:
        return True

    #Top to Bottoms
    elif board[0] == sign and board[3] == sign and board[6] == sign:
        return True
    elif board[1] == sign and board[4] == sign and board[7] == sign:
        return True
    elif board[2] == sign and board[5] == sign and board[8] == sign:
        return True
    
    #Diagonals
    elif board[0] == sign and board[4] == sign and board[8] == sign:
        return True
    elif board[2] == sign and board[4] == sign and board[6] == sign:
        return True

def win(winner):
    clearTerminal()
    showBoard()

    print(winner + " HAS WON!")

    playAgain()

def changeGlobalBoard(index, sign):
    BOARD[index] = sign

def tie():
    if " " not in getBoard():
        showBoard()

        print("TIE")
        playAgain()

def playAgain():
    playAgain = ""
    
    while playAgain == "":
        playAgain = input("Would you like to play again?: ")
    
    if playAgain.lower().startswith("y"):
        os.system("clear")
        main()
    else:
        sys.exit()

def main():
    clearTerminal()
    global BOARD, COMPUTERSIGN, PLAYERSIGN

    BOARD = [" "," "," "," "," "," "," "," "," "]
    COMPUTERSIGN = ""
    PLAYERSIGN = ""

    while PLAYERSIGN == "":
        PLAYERSIGN = input("Would you like to be X or O?: ")
    
    if PLAYERSIGN.lower() == "x":
        COMPUTERSIGN = "O"
        playerTurn()
    else:
        COMPUTERSIGN = "X"
        computerTurn()

main()