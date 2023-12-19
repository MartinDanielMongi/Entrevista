import pprint
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.modules.fight import fight
from src.modules.player1 import TonynStallone, ArnaldorShuatseneguer

router = APIRouter(tags=["Fight"])


@router.post("/fight")
def start_fight(player1: TonynStallone, player2: ArnaldorShuatseneguer):
    logs = fight(player1, player2)
    print(*logs)
    pprint.pprint(logs)
    pretty_logs="\n".join(logs)
    print(pretty_logs)
    return JSONResponse(content=logs, status_code=200)
