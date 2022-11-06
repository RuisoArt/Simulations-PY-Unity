# reference: https://www.youtube.com/watch?v=qPtKv9fSHZY&t=474s&ab_channel=DotCSV

# pip install pygame
# pip install numpy

import pygame
import numpy as np
import time

from Keyboard import bucles_teclado as key
import InitPyGameParameters as params
import InitGameState as gm
import InitPolygon as poly

# Definir el numero e ciclos
myKeyboard = key()
print("El numero de bucles es de : ", myKeyboard)

#inicializa el ambiente pygame
pygame.init() 
width, height = params.width , params.height
screen = pygame.display.set_mode((height, width))
background = params.background
screen.fill(background)

# cantidad de celdas del tablero
n_celdas_x, n_celdas_y = params.number_celdas_axis_x , params.number_celdas_axis_y
# ancho y alto de las celdas del tablero
dimensionW = params.dimensionsCeldaWidth
dimensionH = params.dimensionsCeldaHeight

# Estado de las celdas inicial en 0 (Vivo=1 , Muerto=0)
gameState = np.zeros((n_celdas_x, n_celdas_y))
# Celdas iniciales con las que empezar el "juego"
gm.one_player(gameState)

contador = 1
#bucle de ejecucion
while True:

    #Copia del estado actual del juego por cada ciclo
    newGameState = np.copy(gameState)
    # Limpiar de informacion la pantalla por cada iteracion
    screen.fill(background)
    time.sleep(0.25)
    
    for y in range(0,n_celdas_x):
        for x in range(0,n_celdas_y):
            n_neighbour = gm.neighbour_states(gameState,x,y,n_celdas_x, n_celdas_y)

            #Reglas
            #Regla 1: Una celula muerta con exactamente 3 vecinos vivos, "revive"
            if gameState[x,y] == 0 and n_neighbour == 3:
                newGameState[x,y] = 1
            #Regla 2: Una celula viva con menos de 2 vecinos vivos, "muere"
            elif gameState[x,y] == 1 and n_neighbour < 2:
                newGameState[x,y] = 0
            #Regla 3: Una celula viva con dos vecinos vivos, "vive"
            elif gameState[x,y] == 1 and n_neighbour == 2:
                newGameState[x,y] = 1
            #Regla 4: Una celula viva con mas de tres vecinos vivos, "muere"
            elif gameState[x,y] == 1 and n_neighbour > 3:
                newGameState[x,y] = 0

            polygon = poly.dimensions_polygon(x,y,dimensionW,dimensionH)

            # Seccion de dibujado de celda por cada par de coordenadas (x,y)
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128,128,128), polygon, 1)
            else:
                pygame.draw.polygon(screen, (199,0,57), polygon, 0)
    
    #Se Actualiza el estado del juego
    gameState = np.copy(newGameState)
    # Se Actualiza la pantalla
    pygame.display.flip()

    contador = contador + 1
    if(contador == myKeyboard):
        break
    else:
        pass

print("Se ejecutaron en total: ",contador," numero de bucles")