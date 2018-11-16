import sys
sys.path.append('../src/')

import classes

def test_occupied_state():
    player = classes.Player("testplayer", "x")
    field = classes.Field()

    field.occupy(player)

    assert field.isOccupied()
    assert field.isOccupiedByPlayer(player)