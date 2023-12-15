from fastapi import APIRouter
from fastapi.responses import JSONResponse
from src.modules.fight import fight
from src.modules.player1 import TonynStallone, ArnaldorShuatseneguer

router = APIRouter(tags=["Fight"])


@router.post("/fight")
def start_fight(player1: TonynStallone, player2: ArnaldorShuatseneguer):
    winner = fight(player1, player2)
    return JSONResponse(content=winner, status_code=200)
