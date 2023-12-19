from src.modules.damage import check_combos
from src.modules.damage import calculate_damage
from src.modules.player1 import TonynStallone
def create_player():
    return TonynStallone(
        movimientos=["","","","",""],
        golpes=["","","","",""]
    )

def test_if_combo1_works():
    complete="PDSD"
    damage=check_combos(create_player(), complete)
    assert damage==["PDSD", 3, "usa un Taladoken"]

def test_if_combo2_works():
    complete="KDS"
    damage=check_combos(create_player(), complete)
    assert damage==["KDS", 2, "conecta un Remuyuken"]

def test_if_combo3_works():
    complete="P"
    damage=check_combos(create_player(), complete)
    assert damage==["P", 1, "da un puñetazo"]

def test_if_combo4_works():
    complete="K"
    damage=check_combos(create_player(), complete)
    assert damage==["K", 1,"da una patada"]

def test_no_combo_detected():
    complete=""
    damage=check_combos(create_player(), complete)
    assert damage==["",0, "se mueve"]

def test_calculate_damage_with_combo1():
    mov="DSD"
    hit="P"
    damage= calculate_damage(mov, hit, create_player())
    assert damage==["PDSD", 3, "usa un Taladoken"]

def test_calculate_damage_with_combo2():
    mov="DASD"
    hit="K"
    damage= calculate_damage(mov, hit, create_player())
    assert damage==["KDS", 2, "conecta un Remuyuken"]

def test_calculate_damage_with_combo3():
    mov="S"
    hit="P"
    damage= calculate_damage(mov, hit, create_player())
    assert damage==["P", 1, "da un puñetazo"]

def test_calculate_damage_with_combo4():
    mov="DS"
    hit="K"
    damage= calculate_damage(mov, hit, create_player())
    assert damage==["K", 1, "da una patada"]