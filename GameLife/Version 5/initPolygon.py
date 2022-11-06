import numpy as np

"""
             Coodernadas del poligono

              (x,y) |---------| (x+1,y)
                    |         |
                    |         |
            (x,y+1) |---------| (x+1 , y+1)
"""

def dimensions_polygon(x, y, widthAxis, heightAxis):
    rectangle = [((x)  * widthAxis , y     * heightAxis),  #Punto x, y (Lado superior Izquierdo)
                ((x+1) * widthAxis , y     * heightAxis), #Punto  (x+1), y (Lado superior Derecho)
                ((x+1) * widthAxis , (y+1) * heightAxis), #Punto (x+1), (y+1) (Lado inferior Derecho)
                ((x)   * widthAxis , (y+1) * heightAxis)] #Punto x, (y,1) (Lado inferior Izquierdo)

    return rectangle
