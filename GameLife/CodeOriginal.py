# reference: https://www.youtube.com/watch?v=qPtKv9fSHZY&t=474s&ab_channel=DotCSV

# pip install pygame
# pip install numpy

import pygame
import numpy as np
import time

pygame.init() #inicializa el ambiente pygame

width, height = 500, 500 #tamaño de tablero
screen = pygame.display.set_mode((height, width))

background = 25, 25, 25 #color de fondo del tablero
screen.fill(background)

# cantidad de celdas del tablero
n_celdas_x, n_celdas_y = 25 , 25
# ancho y alto de las celdas del tablero
dimensionsCeldaWidth = width/n_celdas_x
dimensionsCeldaHeight = height/n_celdas_y

# Estado de las celdas inicial en 0 (Vivo=1 , Muerto=0)
gameState = np.zeros((n_celdas_x, n_celdas_y))

# Celdas iniciales con las que empezar el "juego"
gameState[21,21] = 1
gameState[22,22] = 1
gameState[22,23] = 1
gameState[21,23] = 1
gameState[20,23] = 1

#bucle de ejecucion
while True:

    #Copia del estado actual del juego por cada ciclo
    newGameState = np.copy(gameState)
    # Limpiar de informacion la pantalla por cada iteracion
    screen.fill(background)
    time.sleep(0.25)
    
    for y in range(0,n_celdas_x):
        for x in range(0,n_celdas_y):
            """
            Vecinos = Neighbour
            [][][]          [(x-1 , y-1)] [(x , y-1)] [(x+1 , y-1)]
            [][][]    =>    [(x-1 , y)  ] [(x , y)  ] [(x+1 , y)  ]
            [][][]          [(x-1 , y+1)] [(x , y+1)] [(x+1 , y+1)]
            """
            #Calculo de vecinos cercanos
            n_neighbour =   gameState[(x-1)%n_celdas_x , (y-1)%n_celdas_y ] + \
                            gameState[(x)%n_celdas_x   , (y-1)%n_celdas_y ] + \
                            gameState[(x+1)%n_celdas_x , (y-1)%n_celdas_y ] + \
                            gameState[(x-1)%n_celdas_x , (y)%n_celdas_y   ] + \
                            gameState[(x+1)%n_celdas_x , (y)%n_celdas_y   ] + \
                            gameState[(x-1)%n_celdas_x , (y+1)%n_celdas_y ] + \
                            gameState[(x)%n_celdas_x   , (y+1)%n_celdas_y ] + \
                            gameState[(x+1)%n_celdas_x , (y+1)%n_celdas_y ]

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

            """
            Coodernadas del poligono
              (x,y) |---------| (x+1,y)
                    |         |
                    |         |
            (x,y+1) |---------| (x+1 , y+1)
            """
            polygon = [
                ( (x) * dimensionsCeldaWidth , (y) * dimensionsCeldaWidth ),
                ( (x+1) * dimensionsCeldaWidth , (y) * dimensionsCeldaHeight ),
                ( (x+1) * dimensionsCeldaWidth , (y+1) * dimensionsCeldaHeight ),
                ( (x) * dimensionsCeldaWidth , (y+1) * dimensionsCeldaHeight)
            ]

            # Seccion de dibujado de celda por cada par de coordenadas (x,y)
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen, (128,128,128), polygon, 1)
            else:
                pygame.draw.polygon(screen, (199,0,57), polygon, 0)
    
    #Se Actualiza el estado del juego
    gameState = np.copy(newGameState)
    # Se Actualiza la pantalla
    pygame.display.flip()
