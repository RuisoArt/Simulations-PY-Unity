"""
Universidad Santo Tomas seccional Tunja
Facultad de Ingenieria de Sistemas
Simulacion
PhD. Msc. Esp. Ing. Juan Francisco Mendoza Moreno.
Est. Angel Manuel Correa Rivera.
Est. Hugo Emmanuel Hernandez Ramirez.
Ing. Est. Luis Felipe Narvaez Gomez.
2022-2
"""

# Librerias Generales
import pygame
import numpy as np
import time
import matplotlib.pyplot as plt
# Librerias Especificas personalizadas
import keyboard as key
import initGameState as gm
import initNeighbour as nb
import initPolygon as poly
import printConsoleAux as cli
import calcMarkov as calc


#Numero de Bucles:
myKeyboard = key.bucles_teclado()
print("El numero de bucles es de : ", myKeyboard)

pygame.init() #Inicializamos el juego
 
ancho, altura = 800, 800 #1000 Asignamos los pixeles a la pantalla.
pantalla = pygame.display.set_mode((altura, ancho)) #Creamos la pantalla

background = 25, 25, 25 #background de pantalla, con los colores de intensidad.
pantalla.fill(background) #Rellenamos la pantalla

axisX, axisY = 55, 55 #Determinar cuantas celdas se quieren en los 2 ejes
widthAxis = ancho / axisX #Ancho de las celdas
heightAxis = altura / axisY #Altura de las celdas


ViViFINAL = 0
ViMuFINAL = 0
MuMuFINAL = 0
MuViFINAL = 0

gameState = np.zeros((axisX, axisY)) #Guardar todos los estados de las diferentes celdas. 1 = viva, 0 = muerta
                                    #zeros(dimensiones) : Crea y devuelve una referencia a un array cuyos elementos son todos ceros.
gm.one_player(gameState)

#control de la ejecucion en el juego
pausa = False 

count = 0
epoca = 0
#zeros(dimensiones) : Crea y devuelve una referencia a un array cuyos elementos son todos ceros.
while count < myKeyboard: #Bucles que recorren cada una de las celdas
    epoca = epoca + 1
    count = count + 1
    ViVi = 0
    ViMu = 0
    MuMu = 0
    MuVi = 0

    nuevasgameState = np.copy(gameState) #Evitamos que los cambios se hagan de forma secuencial, y hace que sean todos de una.
    pantalla.fill(background)
    time.sleep(0.2)

    pulsaciones =  pygame.event.get() #Registro de pulsaciones en el teclado o mouse

    for event in pulsaciones:
        #Deteccion de pulsacion de cualquier tecla de teclado
        if event.type ==pygame.KEYDOWN: 
            #cambio de la variable pausa si se oprime una tecla
            pausa = not pausa 
        
    for y in range(0, axisX):

        
        for x in range(0, axisY):

             #El if da la pausa del proceso en caso de ser pulsada alguna tecla 
            if not pausa: 

            

                poblacionInicial = ViVi
                poblacionFinal = ViViFINAL + MuViFINAL

                contarVecinos = nb.neighbour_states(gameState, x, y, axisX, axisY)

                #Rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
                if gameState [x,y] == 1 and (contarVecinos < 2 or contarVecinos > 3):
                    nuevasgameState[x, y] = 0
                    ViMu = ViMu + 1
                    ViMuFINAL = ViMuFINAL + 1


                #Rule 2: Any live cell with two or three live neighbours lives on to the next generation.
                elif gameState [x,y] == 1 and (contarVecinos == 2 or contarVecinos == 3):
                    nuevasgameState[x,y] = 1
                    ViVi = ViVi + 1
                    ViViFINAL = ViViFINAL + 1


                #Rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation.
                #elif gameState[x, y] == 1 and (contarVecinos > 3):
                #   nuevasgameState[x, y] = 0
                #  ViMu = ViMu + 1

                #Rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
                elif gameState[x, y] == 0 and contarVecinos ==3:
                    nuevasgameState[x, y] = 1
                    MuVi = MuVi + 1
                    MuViFINAL = MuViFINAL + 1

                else:
                    MuMu = MuMu + 1
                    MuMuFINAL = MuMuFINAL + 1


                # Los puntos que defienen al poligono
                CUADRADO =  poly.dimensions_polygon(x, y, widthAxis, heightAxis)

                if nuevasgameState[x, y] == 0:
                    pygame.draw.polygon(pantalla,(128, 128, 128), CUADRADO, 1) #Dibujar la pantalla para celula muerta
                else:
                    pygame.draw.polygon(pantalla, (180, 90, 110), CUADRADO, 0)  # Dibujar la pantalla para celula viva

    #El if da la pausa en caso de ser pulsada alguna tecla 
    if not pausa: 
        cli.markov_count(epoca, poblacionInicial, ViVi, ViMu, MuMu, MuVi)
        TransitionStates = calc.estados_transicion
        TransitionMatrix = calc.bucle_calc_markov(ViVi, MuVi, MuMu, ViMu)
        print(TransitionMatrix)

        gameState = np.copy(nuevasgameState)  # Nuestro estado es el nuevo estado
        pygame.display.flip()


cli.finished_markov(epoca, poblacionFinal, ViViFINAL, ViMuFINAL, MuMuFINAL, MuViFINAL)
TransitionStates = calc.estados_transicion
TransitionMatrix = calc.finish_calc_markov(ViViFINAL,ViMuFINAL,MuMuFINAL,MuViFINAL)
print(TransitionMatrix)








