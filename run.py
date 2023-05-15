# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

gameBoard = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

game = True
winner = None
player = "X"


# game structure
def printBoard(gameBoard):
    print(gameBoard[0] + " | " + gameBoard[1] + " | " + gameBoard[2])
    print(gameBoard[3] + " | " + gameBoard[4] + " | " + gameBoard[5])
    print(gameBoard[6] + " | " + gameBoard[7] + " | " + gameBoard[8])


# player input
def playerInput(gameBoard):
    inp = int(input("Select a spot 1-9: "))
    if inp >= 1 and inp <= 9 and gameBoard[inp-1] == "-":
        gameBoard[inp-1] = player
    else:
        print("Player is already at that spot.")


# winning or tying
def checkHorizontle(gameBoard):
    global winner
    if gameBoard[0] == gameBoard[1] == gameBoard[2] and gameBoard[0] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[3] == gameBoard[4] == gameBoard[5] and gameBoard[3] != "-":
        winner = gameBoard[3]
        return True
    elif gameBoard[6] == gameBoard[7] == gameBoard[8] and gameBoard[6] != "-":
        winner = gameBoard[6]
        return True


def checkRow(gameBoard):
    global winner
    if gameBoard[0] == gameBoard[3] == gameBoard[6] and gameBoard[0] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[1] == gameBoard[4] == gameBoard[7] and gameBoard[1] != "-":
        winner = gameBoard[1]
        return True
    elif gameBoard[2] == gameBoard[5] == gameBoard[8] and gameBoard[2] != "-":
        winner = gameBoard[3]
        return True


def checkDiagonal(gameBoard):
    global winner
    if gameBoard[0] == gameBoard[4] == gameBoard[8] and gameBoard[0] != "-":
        winner = gameBoard[0]
        return True
    elif gameBoard[2] == gameBoard[4] == gameBoard[6] and gameBoard[4] != "-":
        winner = gameBoard[2]
        return True


def checkIfWin(gameBoard):
    global game
    if checkHorizontle(gameBoard):
        printBoard(gameBoard)
        print(f"The winner is {winner}!")
        game = False

    elif checkRow(gameBoard):
        printBoard(gameBoard)
        print(f"The winner is {winner}!")
        game = False

    elif checkDiagonal(gameBoard):
        printBoard(gameBoard)
        print(f"The winner is {winner}!")
        game = False


def checkIfTie(gameBoard):
    global game
    if "-" not in gameBoard:
        printBoard(gameBoard)
        print("It is a tie!")
        game = False


# change player
def changePlayer(gameBoard):
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


def computer(gameBoard):
    while player == "O":
        position = random.randint(0, 8)
        if gameBoard[position] == "-":
            gameBoard[position] = "O"
            changePlayer(gameBoard)


# main
while game:
    printBoard(gameBoard)
    playerInput(gameBoard)
    checkIfWin(gameBoard)
    checkIfTie(gameBoard)
    changePlayer(gameBoard)
    computer(gameBoard)
    checkIfWin(gameBoard)
    checkIfTie(gameBoard)
