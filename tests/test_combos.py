from src.modules.combos import check_combos
from src.modules.player1 import TonynStallone
def create_player():
    return TonynStallone(
        movimientos=["","","","",""],
        golpes=["","","","",""]
    )
def test_combo1():
    complete="PDSD"
    damage=check_combos(create_player(), complete)
    assert damage==["PDSD", 3, "usa un Taladoken"]

def test_combo2():
    complete="KDS"
    damage=check_combos(create_player(), complete)
    assert damage==["KDS", 2, "conecta un Remuyuken"]

def test_combo3():
    complete="P"
    damage=check_combos(create_player(), complete)
    assert damage==["P", 1, "da un puñetazo"]

def test_combo4():
    complete="K"
    damage=check_combos(create_player(), complete)
    assert damage==["K", 1,"da una patada"]

def test_no_combo_detected():
    complete=""
    damage=check_combos(create_player(), complete)
    assert damage==["",0, "se mueve"]