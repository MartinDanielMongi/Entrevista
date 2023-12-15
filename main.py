from fastapi import FastAPI
from controller import router
from modules.player1 import Player

app = FastAPI()
app.include_router(router)

