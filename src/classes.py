import re

class Game:
    def __init__(self, player1, player2):
        self.fields = [Field() for i in range(9)]
        self.player1 = player1
        self.player2 = player2

    # display fields the way your numpad is configured for the best
    # user experience (7 is top left, 3 is bottom right, etc.)
    def __drawBoard(self):
        fieldCount = 0
        for field in (self.fields[6:9] + self.fields[3:6] + self.fields[0:3]):
            print(field.draw(), end = "" if fieldCount % 3 != 2 else "\n" )
            fieldCount += 1
    
    def __isFinished(self):
        def boardIsFull():
            return all(field.isOccupied() for field in self.fields)

        def hasWinner():
            return self.player1.isWinner(self.fields) or self.player2.isWinner(self.fields)

        return boardIsFull() or hasWinner()

    def play(self):
        activePlayer = self.player2
        self.__drawBoard()
        
        while not self.__isFinished():
            activePlayer = activePlayer.otherPlayer
            occupyFieldNr = ""

            def isValidInput(tryingToOccupyFieldNr):
                return re.compile("^[1-9]{1}$").match(tryingToOccupyFieldNr) and not self.fields[int(tryingToOccupyFieldNr)-1].isOccupied()

            while not isValidInput(occupyFieldNr):
                occupyFieldNr = input(f"{activePlayer.name} ({activePlayer.mark}), make your move (1-9)):")
            
            self.fields[int(occupyFieldNr)-1].occupy(activePlayer)
            self.__drawBoard()

    def getWinner(self):
        if (self.player1.isWinner(self.fields)):
            return self.player1
        elif (self.player2.isWinner(self.fields)):
            return self.player2
        
        return None

class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        self.otherPlayer = None
    
    def isWinner(self, fields):
        # In order; row 1, 2, 3; diagonal 1, 2; column 1, 2, 3;
        return all(field.isOccupiedByPlayer(self) for field in fields[0:3]) or \
            all(field.isOccupiedByPlayer(self) for field in fields[3:6]) or \
            all(field.isOccupiedByPlayer(self) for field in fields[6:9]) or \
            all(field.isOccupiedByPlayer(self) for field in fields[0:9:4]) or \
            all(field.isOccupiedByPlayer(self) for field in fields[2:7:2]) or \
            all(field.isOccupiedByPlayer(self) for field in fields[0:7:3]) or \
            all(field.isOccupiedByPlayer(self) for field in fields[1:8:3]) or \
            all(field.isOccupiedByPlayer(self) for field in fields[2:9:3])

class Field:
    def __init__(self):
        self.player = None

    def isOccupied(self):
        return self.player is not None

    def isOccupiedByPlayer(self, player):
        return self.player == player

    def occupy(self, player):
        self.player = player

    def draw(self):
        return " " + self.player.mark + " " if self.isOccupied() else " _ "