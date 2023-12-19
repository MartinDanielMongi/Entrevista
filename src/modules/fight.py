from src.modules.starter import calculate_first_to_play
from src.modules.damage import calculate_damage
from src.modules.player1 import Player

TOTAL_TURN = 5


def fight(player1: Player, player2: Player):
    logs=[]
    first = calculate_first_to_play(player1, player2)
    if first is player1:
        second = player2
    else:
        second = player1
    for x in range(TOTAL_TURN):
        damageReceived = calculate_damage(
            first.movements[x], first.hits[x], first
        )  # Llamo a una funcion que se encarga de ver cuando daño hizo
        second.hp -= damageReceived[1]
        logs.append(f"{first.name} {damageReceived[2]}")
        if second.hp >= 0:
            damageReceived = calculate_damage(
                second.movements[x], second.hits[x], second
            )
            first.hp -= damageReceived[1]
            logs.append(f"{second.name} {damageReceived[2]}")
        else:
            logs.append(f"{first.name} gana la batalla, y aun le queda {first.hp} de vida")
            return logs
        if first.hp <= 0:
            logs.append(f"{second.name} gana la batalla, y aun le queda {second.hp} de vida")
            return logs
    logs.append("Se quedaron sin turnos!")
    return logs
