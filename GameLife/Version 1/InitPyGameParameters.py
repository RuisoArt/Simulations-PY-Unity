import pygame

width, height = 500, 500 #tamaño de tablero
screen = pygame.display.set_mode((height, width))
background = 25, 25, 25 #color de fondo del tablero

# cantidad de celdas del tablero
number_celdas_axis_x, number_celdas_axis_y = 25 , 25

# ancho y alto de las celdas del tablero
dimensionsCeldaWidth = width/number_celdas_axis_x
dimensionsCeldaHeight = height/number_celdas_axis_y