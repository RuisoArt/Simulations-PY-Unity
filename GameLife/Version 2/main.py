import pygame
import numpy as np
import time
import matplotlib.pyplot as plt

#Angel Manuel Correa Rivera
#GameOfLife
pygame.init() #Inicializamos el juego


ancho, altura = 800, 800 #1000 Asignamos los pixeles a la pantalla.
pantalla = pygame.display.set_mode((altura, ancho)) #Creamos la pantalla

fondo = 25, 25, 25 #Fondo de pantalla, con los colores de intensidad.
pantalla.fill(fondo) #Rellenamos la pantalla

ejeX, ejeY = 25, 25 #Determinar cuantas celdas se quieren en los 2 ejes
anchoEje = ancho / ejeX #Ancho de las celdas
alturaEje = altura / ejeY #Altura de las celdas


ViViFINAL = 0
ViMuFINAL = 0
MuMuFINAL = 0
MuViFINAL = 0





celulas = np.zeros((ejeX, ejeY)) #Guardar todos los estados de las diferentes celdas. 1 = viva, 0 = muerta
#zeros(dimensiones) : Crea y devuelve una referencia a un array cuyos elementos son todos ceros.

celulas[6,4] = 1
celulas[6,5] = 1
celulas[6,6] = 1
celulas[5,6] = 1
celulas[4,5]= 1

count = 0
epoca = 0
#zeros(dimensiones) : Crea y devuelve una referencia a un array cuyos elementos son todos ceros.
while count < 5: #Bucles que recorren cada una de las celdas
    epoca = epoca + 1
    count = count + 1
    ViVi = 0
    ViMu = 0
    MuMu = 0
    MuVi = 0

    nuevasCelulas = np.copy(celulas) #Evitamos que los cambios se hagan de forma secuencial, y hace que sean todos de una.
    pantalla.fill(fondo)
    time.sleep(1)


    for y in range(0, ejeX):
        for x in range(0, ejeY):

            poblacionInicial = ViVi
            poblacionFinal = ViViFINAL + MuViFINAL


            # Calcular el numero de vecinos
            # Celda Diagonal Superior Izquierda
            # Celda Superior
            # Celda Diagonal Superior Derecha
            # Celda Izquierda
            # Celda Derecha
            # Celda Diagonal Inferior Izquierda
            # Celda Inferior
            # Celda Diagonal Inferior Derecha

            ## % ejeX, %ejeY Se accede al tamaño del numero de la celda.
            contarVecinos = celulas[(x-1) % ejeX, (y-1) % ejeY] + \
                            celulas[(x) % ejeX, (y-1) % ejeY] + \
                            celulas[(x+1) % ejeX, (y-1) % ejeY] + \
                            celulas[(x-1) % ejeX, (y) % ejeY] + \
                            celulas[(x+1) % ejeX, (y) % ejeY] + \
                            celulas[(x-1) % ejeX, (y+1) % ejeY] + \
                            celulas[(x) % ejeX, (y+1) %ejeY] + \
                            celulas[(x+1) %ejeX, (y+1) %ejeY]



            #Rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            if celulas [x,y] == 1 and (contarVecinos < 2 or contarVecinos > 3):
                nuevasCelulas[x, y] = 0
                ViMu = ViMu + 1
                ViMuFINAL = ViMuFINAL + 1


            #Rule 2: Any live cell with two or three live neighbours lives on to the next generation.
            elif celulas [x,y] == 1 and (contarVecinos == 2 or contarVecinos == 3):
                nuevasCelulas[x,y] = 1
                ViVi = ViVi + 1
                ViViFINAL = ViViFINAL + 1


            #Rule 3: Any live cell with more than three live neighbours dies, as if by overpopulation.
            #elif celulas[x, y] == 1 and (contarVecinos > 3):
             #   nuevasCelulas[x, y] = 0
              #  ViMu = ViMu + 1

            #Rule 4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            elif celulas[x, y] == 0 and contarVecinos ==3:
                nuevasCelulas[x, y] = 1
                MuVi = MuVi + 1
                MuViFINAL = MuViFINAL + 1

            else:
                MuMu = MuMu + 1
                MuMuFINAL = MuMuFINAL + 1
            # Los puntos que defienen al poligono
            CUADRADO =  [((x) * anchoEje, y * alturaEje),  #Punto x, y (Lado superior Izquierdo)
                     ((x+1) * anchoEje, y * alturaEje), #Punto  (x+1), y (Lado superior Derecho)
                     ((x+1) * anchoEje, (y+1) * alturaEje), #Punto (x+1), (y+1) (Lado inferior Derecho)
                     ((x) * anchoEje, (y+1) * alturaEje)] #Punto x, (y,1) (Lado inferior Izquierdo)

            if nuevasCelulas[x, y] == 0:
                pygame.draw.polygon(pantalla,(128, 128, 128), CUADRADO, 1) #Dibujar la pantalla para celula muerta
            else:
                pygame.draw.polygon(pantalla, (180, 90, 110), CUADRADO, 0)  # Dibujar la pantalla para celula viva

    print("════════════════════════════════════════════════════════════════════")
    print("Epoca: ", epoca)
    print("La poblacion de la epoca ", " es de : ", poblacionInicial)
    print("La poblacion que permanecio viva es de : ", ViVi)
    print("La poblacion que murio fue de : ", ViMu)
    print("La poblacion que se matuvo muerta es de : ", MuMu)
    print("La poblacion que revivio con las esferas del dragon es de : ", MuVi)
    print("════════════════════════════════════════════════════════════════════")
    TransitionStates = [["ViVi", "ViMu"], ["MuVi", "MuMu"]]
    TransitionMatrix = [[(ViVi / (ViVi + ViMu)), (ViMu / (ViVi+ ViMu))],
                        [(MuVi / (MuVi + MuMu)), (MuMu / (MuVi + MuMu))]]
    print(TransitionMatrix)

    celulas = np.copy(nuevasCelulas)  # Nuestro estado es el nuevo estado
    pygame.display.flip()


print("═══════════════════════════════════════════════════════════════════════")
print("El total de epocas fueron: ", epoca)
print("La poblacion de todas las generaciones fue de : ", poblacionFinal)
print("La poblacion que permanecio viva en general fue de : ", ViViFINAL)
print("La poblacion que paso de viva a muerta en general fue de  : ", ViMuFINAL)
print("La poblacion que se mantuvo muerta en toda la simulacion fue de : ", MuMuFINAL)
print("La poblacion que revivio en general con las esferas del dragon es de : ", MuViFINAL)
print("══════════════════════════════════════════════════════════════════════")

TransitionStates = [["ViVi","ViMu"],["MuVi","MuMu"]] #Dos dimensiones, lista dentro otra lista [matriz], para las 4 posibles trasiciones
TransitionMatrix = [[(ViViFINAL/(ViViFINAL+ViMuFINAL)),(ViMuFINAL/(ViViFINAL+ViMuFINAL))],
                    [(MuViFINAL/(MuViFINAL+MuMuFINAL)),(MuMuFINAL/(MuViFINAL+MuMuFINAL))]] #Matriz de transicion
print(TransitionMatrix)








