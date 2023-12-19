from src.modules.starter import calculate_first_to_play
from src.modules.player1 import Player
from src.modules.player1 import TonynStallone
from src.modules.player1 import ArnaldorShuatseneguer

def test_Tonyn_starts_less_actions():
    player1=TonynStallone(
        movimientos=["AD","AS","AS","SD","AD"],
        golpes=["K","P","P","P","",""]
    )
    player2=ArnaldorShuatseneguer(
        movimientos=["ASD","ASD","ASD","ASD","ASD"],
        golpes=["K","K","K","K","K","K"]
    )
    first= calculate_first_to_play(player1, player2)

    assert first==player1

def test_Arnaldor_starts_less_actions():
    player1=TonynStallone(
        movimientos=["ASD","ASD","ASD","ASD","ASD"],
        golpes=["K","K","K","K","K","K"]

    )
    player2=ArnaldorShuatseneguer(
        movimientos=["AD","AS","AS","SD","AD"],
        golpes=["K","P","P","P","",""]
    )
    first= calculate_first_to_play(player1, player2)

    assert first==player2

def test_Tonyn_starts_less_movements():
    player1=TonynStallone(
        movimientos=["A","","","",""],
        golpes=["","","","","",""]
    )
    player2=ArnaldorShuatseneguer(
        movimientos=["","","","",""],
        golpes=["K","","","","",""]
    )
    first= calculate_first_to_play(player1, player2)

    assert first==player2

def test_Arnol_starts_less_movements():
    player1=TonynStallone(
        movimientos=["","","","",""],
        golpes=["K","","","","",""]

    )
    player2=ArnaldorShuatseneguer(
        movimientos=["A","","","",""],
        golpes=["","","","","",""]
    )
    first= calculate_first_to_play(player1, player2)

    assert first==player1

def test_Tonyn_starts_draw():
    player1=TonynStallone(
        movimientos=["ASD","ASD","ASD","ASD","ASD"],
        golpes=["K","K","K","K","K","K"]

    )
    player2=ArnaldorShuatseneguer(
        movimientos=["ASD","ASD","ASD","ASD","ASD"],
        golpes=["K","K","K","K","K","K"]
    )
    first= calculate_first_to_play(player1, player2)

    assert first==player1
    