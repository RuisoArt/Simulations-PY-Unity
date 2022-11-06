import pygame
import numpy as np
import time

# Celdas iniciales con las que empezar el "juego"
def one_player(gameState):
    gameState[21,21] = 1
    gameState[22,22] = 1
    gameState[22,23] = 1
    gameState[21,23] = 1
    gameState[20,23] = 1


"""
            Calculo de vecinos cercanos

                Vecinos = Neighbour

[][][]          [(x-1 , y-1)] [(x , y-1)] [(x+1 , y-1)]
[][][]    =>    [(x-1 , y)  ] [(x , y)  ] [(x+1 , y)  ]
[][][]          [(x-1 , y+1)] [(x , y+1)] [(x+1 , y+1)]
"""
def neighbour_states(gameState,x,y,n_celdas_x, n_celdas_y):
    n_neighbour =   gameState[(x-1)%n_celdas_x , (y-1)%n_celdas_y ] + \
                    gameState[(x)%n_celdas_x   , (y-1)%n_celdas_y ] + \
                    gameState[(x+1)%n_celdas_x , (y-1)%n_celdas_y ] + \
                    gameState[(x-1)%n_celdas_x , (y)%n_celdas_y   ] + \
                    gameState[(x+1)%n_celdas_x , (y)%n_celdas_y   ] + \
                    gameState[(x-1)%n_celdas_x , (y+1)%n_celdas_y ] + \
                    gameState[(x)%n_celdas_x   , (y+1)%n_celdas_y ] + \
                    gameState[(x+1)%n_celdas_x , (y+1)%n_celdas_y ]

    return n_neighbour