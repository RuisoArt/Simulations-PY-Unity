import numpy as np

# Celdas iniciales con las que empezar el "juego"
def one_player(gameState):
    gameState[6,4] = 1
    gameState[6,5] = 1
    gameState[6,6] = 1
    gameState[5,6] = 1
    gameState[4,5] = 1
