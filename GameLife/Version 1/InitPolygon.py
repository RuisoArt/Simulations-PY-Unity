import pygame
import numpy as np
import time


"""
             Coodernadas del poligono

              (x,y) |---------| (x+1,y)
                    |         |
                    |         |
            (x,y+1) |---------| (x+1 , y+1)
"""
def dimensions_polygon(x,y,dimensionW,dimensionH):
    polygon = [
                ( (x) * dimensionW , (y) * dimensionH ),
                ( (x+1) * dimensionW , (y) * dimensionH ),
                ( (x+1) * dimensionW , (y+1) * dimensionH ),
                ( (x) * dimensionW , (y+1) * dimensionH)
            ]
    return polygon
