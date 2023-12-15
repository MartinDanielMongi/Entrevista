from fastapi import FastAPI
from src.controller import router
from src.modules.player1 import Player

app = FastAPI()
app.include_router(router)
