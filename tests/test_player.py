import sys
sys.path.append('../src/')

import pytest
import classes

@pytest.mark.parametrize(
    'winField1, winField2, winField3', [
        (0,1,2), # row 1
        (3,4,5), # row 2
        (6,7,8), # row 3
        (0,3,6), # column 1
        (1,4,7), # column 2
        (2,5,8), # column 3
        (0,4,8), # diagonal 1
        (2,4,6)  # diagonal 2
    ]
)
def test_is_winner(winField1, winField2, winField3):
    player = classes.Player("testplayer", "x")
    fields = [classes.Field() for i in range(9)]

    assert not player.isWinner(fields)

    fields[winField1].occupy(player)
    fields[winField2].occupy(player)
    fields[winField3].occupy(player)

    assert player.isWinner(fields)

@pytest.mark.parametrize(
    'field1, field2, field3', [
        (0,1,3),
        (0,4,5),
        (6,5,8),
        (0,2,6)
    ]
)
def test_is_not_winner(field1, field2, field3):
    player = classes.Player("testplayer", "x")
    fields = [classes.Field() for i in range(9)]

    fields[field1].occupy(player)
    fields[field2].occupy(player)
    fields[field3].occupy(player)

    assert not player.isWinner(fields)