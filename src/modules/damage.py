from src.modules.player1 import Player

def calculate_damage(mov, hit, player):
    complete = mov + hit
    complete = complete[::-1]
    damage = check_combos(player, complete)
    return damage


def check_combos(player:Player, complete):
    if complete[:4]==player.combo1[0]:
        return player.combo1
    if complete[:3]==player.combo2[0]:
        return player.combo2
    if complete[:1]==player.combo3[0]:
        return player.combo3
    if complete[:1]==player.combo4[0]:
        return player.combo4
    else:
        return ["",0, "se mueve"] 

