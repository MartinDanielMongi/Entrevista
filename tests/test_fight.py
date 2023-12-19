from src.modules.fight import fight
from src.modules.player1 import TonynStallone
from src.modules.player1 import ArnaldorShuatseneguer

def test_Arnaldor_wins():
    player1=TonynStallone(
        movimientos=["D","DSD","S","DSD","SD"],
        golpes=["K","P","","K","P"]
    )
    player2=ArnaldorShuatseneguer(
        movimientos=["SA","SA","SA","ASA","SA"],
        golpes=["K","","K","P","P"]
    )
    logs= fight(player1, player2)
    expected_logs=['Tonyn Stallone da una patada',
        'Arnaldor Shuatseneguer conecta un Remuyuken',
        'Tonyn Stallone usa un Taladoken',
        'Arnaldor Shuatseneguer se mueve',
        'Tonyn Stallone se mueve',
        'Arnaldor Shuatseneguer conecta un Remuyuken',
        'Arnaldor Shuatseneguer gana la batalla, y aun le queda 2 de vida'
    ]
    
    assert logs== expected_logs

def test_Tonyn_wins():
    player1=TonynStallone(
        movimientos=["","DSD","","DSD","SD"],
        golpes=["K","P","K","K","P"]
    )
    player2=ArnaldorShuatseneguer(
        movimientos=["SAA","SA","SA","AA","A"],
        golpes=["K","","","P","P"]
    )
    logs= fight(player1, player2)
    expected_logs=[
        'Tonyn Stallone da una patada',
        'Arnaldor Shuatseneguer da una patada',
        'Tonyn Stallone usa un Taladoken',
        'Arnaldor Shuatseneguer se mueve',
        'Tonyn Stallone da una patada',
        'Arnaldor Shuatseneguer se mueve',
        'Tonyn Stallone conecta un Remuyuken',
        'Tonyn Stallone gana la batalla, y aun le queda 5 de vida'
    ]
    
    assert logs== expected_logs