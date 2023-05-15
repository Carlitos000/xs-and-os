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

# change player

while game:
    printBoard(gameBoard)
    input(gameBoard)
