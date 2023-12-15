def check_combos(player, complete):
    if complete[:4] == player.combo1[0]:
        return player.combo1
    if complete[:3] == player.combo2[0]:
        return player.combo2
    if complete[:1] == player.combo3[0]:
        return player.combo3
    if complete[:1] == player.combo4[0]:
        return player.combo4
    else:
        return ["", 0, "se mueve"]
