import re
import os
import classes

def setUpPlayer(playerNr):
    playerName = ""
    playerMark = ""

    def PlayerNamePattern():
        return re.compile("^[a-zA-Z]+$")

    def PlayerMarkPattern():
        return re.compile("^.{1}$")

    while not PlayerNamePattern().match(playerName):
        playerName = input(f"Player {playerNr} name (just letters):")
    while not PlayerMarkPattern().match(playerMark):
        playerMark = input(f"Player {playerNr} choose mark (1 char):")

    return classes.Player(playerName, playerMark)

def program():
    os.system("cls")
    print("Welcome to tic tac toe.\nGive input the way your numpad is configured (top left is 7).")
    player1 = setUpPlayer(1)
    player2 = setUpPlayer(2)
    player1.otherPlayer = player2
    player2.otherPlayer = player1
    game = classes.Game(player1, player2)
    
    game.play()

    winner = game.getWinner()
    print("tie") if winner == None else print(f"congratulations {winner.name}")
    
program()