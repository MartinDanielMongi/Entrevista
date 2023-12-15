from pydantic import BaseModel, Field
from typing import Optional

class Player(BaseModel):
    name: Optional[str]
    hp: Optional[int]=6
    movements: list[str] = Field(alias="movimientos")
    hits: list[str]= Field(alias="golpes")
    combo1: Optional[tuple[str, int, str]]
    combo2: Optional[tuple[str, int, str]]
    combo3: Optional[tuple[str, int, str]]
    combo4: Optional[tuple[str, int, str]]

class TonynStallone(Player):
    name: str="Tonyn Stallone"
    combo1:tuple[str, int, str]= ["PDSD", 3, "usa un Taladoken"]
    combo2:tuple[str, int, str]=  ["KDS", 2, "conecta un Remuyuken"]
    combo3:tuple[str, int, str]=  ["P", 1, "da un puñetazo"]
    combo4:tuple[str, int, str]=  ["K", 1,"da una patada"]

class ArnaldorShuatseneguer(Player):
    name: str="Arnaldor Shuatseneguer"
    combo1:tuple[str, int, str]=  ["PASA", 2, "usa un Taladoken"]
    combo2:tuple[str, int, str]=  ["KAS", 3, "conecta un Remuyuken"]
    combo3:tuple[str, int, str]=  ["P", 1, "da un puñetazo"]
    combo4:tuple[str, int, str]=  ["K", 1,"da una patada"]


