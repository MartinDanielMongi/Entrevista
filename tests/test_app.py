from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_player1_wins():
    input = {
        "player1":
            {
                "movimientos":["SA","SA","SA","ASA","SA"],
                "golpes":["K","","K","P","P"]
            },
        "player2":
            {
                "movimientos":["D","DSD","S","DSD","SD"],
                "golpes":["K","P","","K","P"]
            } 
    }
    response = client.post("/fight", json=input)
    assert response.status_code == 200

# def test_player2_wins():
#     input = {
#         "player1":
#             {
#                 "movimientos":["D","DSD","S","DSD","SD"],
#                 "golpes":["K","P","","K","P"]
#             },
#         "player2":
#             {
#                 "movimientos":["SA","SA","SA","ASA","SA"],
#                 "golpes":["K","","K","P","P"]
#             } 
#     }
#     response = client.post("/Fight", json=input)
#     assert response.status_code == 200
