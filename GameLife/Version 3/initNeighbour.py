import numpy as np

"""
            Calculo de vecinos cercanos

                Vecinos = Neighbour

[][][]          [(x-1 , y-1)] [(x , y-1)] [(x+1 , y-1)]
[][][]    =>    [(x-1 , y)  ] [(x , y)  ] [(x+1 , y)  ]
[][][]          [(x-1 , y+1)] [(x , y+1)] [(x+1 , y+1)]
"""
# Calcular el numero de vecinos
# Celda Diagonal Superior Izquierda
# Celda Superior
# Celda Diagonal Superior Derecha
# Celda Izquierda
# Celda Derecha
# Celda Diagonal Inferior Izquierda
# Celda Inferior
# Celda Diagonal Inferior Derecha


def neighbour_states (gameState, x, y, axisX, axisY):
    ## % axisX, %axisY Se accede al tamaño del numero de la celda.
    n_neighbour =   gameState[(x-1) % axisX , (y-1) % axisY] + \
                    gameState[(x)   % axisX , (y-1) % axisY] + \
                    gameState[(x+1) % axisX , (y-1) % axisY] + \
                    gameState[(x-1) % axisX , (y)   % axisY] + \
                    gameState[(x+1) % axisX , (y)   % axisY] + \
                    gameState[(x-1) % axisX , (y+1) % axisY] + \
                    gameState[(x)   % axisX , (y+1) % axisY] + \
                    gameState[(x+1) % axisX , (y+1) % axisY]

    return n_neighbour