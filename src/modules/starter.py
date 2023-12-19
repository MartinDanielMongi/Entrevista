# Función utilizada para ver quien comienza la partida.
from src.modules.player1 import Player


def calculate_first_to_play(pla1: Player, pla2: Player):
    # Comienzo a extraer todos los botones, para poder ver cual tuvo la menor combinación de botones
    mov1 = "".join(pla1.movements)
    mov2 = "".join(pla2.movements)
    hit1 = "".join(pla1.hits)
    hit2 = "".join(pla2.hits)

    total_movements_1 = len(
        mov1
    )  # Veo la longitud de cada combinacion de botones, para iniciar la comparación
    total_hits_1 = len(hit1)
    total_movements_2 = len(mov2)
    total_hits_2 = len(hit2)
    sum_of_actions_1 = total_movements_1 + total_hits_1
    sum_of_actions_2 = total_movements_2 + total_hits_2

    # Cadena logica para ver quien comienza, y devuelve el diccionario del que empieza

    if sum_of_actions_1 > sum_of_actions_2:
        return pla2
    if sum_of_actions_1 < sum_of_actions_2:
        return pla1
    else:
        if total_movements_1 > total_movements_2:
            return pla2
        if total_movements_1 < total_movements_2:
            return pla1
        else:
            return pla1
