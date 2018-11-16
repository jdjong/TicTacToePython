import sys
sys.path.append('../src/')

import pytest
import classes

@pytest.mark.parametrize(
    'player1WinningInputSequence', [
        ["1", "2", "3", "4", "5", "6", "7"],
        ["1", "2", "4", "3", "7"],
        ["1", "2", "3", "5", "9", "7", "8", "4", "6"], # board is full
    ]
)
def test_player1_is_winner(player1WinningInputSequence):
        player1 = classes.Player("Henk", "X")
        player2 = classes.Player("Ali", "O")
        player1.otherPlayer = player2
        player2.otherPlayer = player1
        game = classes.Game(player1, player2)

        def mock_input(s):
           return player1WinningInputSequence.pop(0)
        classes.input = mock_input

        game.play()

        assert game.getWinner() == player1

@pytest.mark.parametrize(
    'player2WinningInputSequence', [
        ["2", "1", "3", "4", "5", "8", "9", "7"],
        ["1", "2", "4", "5", "9", "8"],
    ]
)
def test_player2_is_winner(player2WinningInputSequence):
        player1 = classes.Player("Henk", "X")
        player2 = classes.Player("Ali", "O")
        player1.otherPlayer = player2
        player2.otherPlayer = player1
        game = classes.Game(player1, player2)

        def mock_input(s):
           return player2WinningInputSequence.pop(0)
        classes.input = mock_input

        game.play()

        assert game.getWinner() == player2

@pytest.mark.parametrize(
    'noWinnerInputSequence', [
        ["5", "1", "9", "6", "8", "7", "4", "2", "3"],
    ]
)
def test_no_winner(noWinnerInputSequence):
        player1 = classes.Player("Henk", "X")
        player2 = classes.Player("Ali", "O")
        player1.otherPlayer = player2
        player2.otherPlayer = player1
        game = classes.Game(player1, player2)

        def mock_input(s):
           return noWinnerInputSequence.pop(0)
        classes.input = mock_input

        game.play()
        
        assert game.getWinner() == None

def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
        classes.input = input  