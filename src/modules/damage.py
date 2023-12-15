from src.modules.player1 import Player
from src.modules.combos import check_combos


def calculate_damage(mov, hit, player):
    complete = mov + hit
    complete = complete[::-1]
    damage = check_combos(player, complete)
    return damage
