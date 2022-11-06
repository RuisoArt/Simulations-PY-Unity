def markov_count(epoca, poblacionInicial, ViVi, ViMu, MuMu, MuVi):
    print("════════════════════════════════════════════════════════════════════")
    print("Epoca: ", epoca)
    print("La poblacion de la epoca ", " es de : ", poblacionInicial)
    print("La poblacion que permanecio viva es de : ", ViVi)
    print("La poblacion que murio fue de : ", ViMu)
    print("La poblacion que se matuvo muerta es de : ", MuMu)
    print("La poblacion que revivio con las esferas del dragon es de : ", MuVi)
    print("════════════════════════════════════════════════════════════════════")

def finished_markov(epoca, poblacionFinal, ViViFINAL, ViMuFINAL, MuMuFINAL, MuViFINAL): 
    print("═══════════════════════════════════════════════════════════════════════")
    print("El total de epocas fueron: ", epoca)
    print("La poblacion de todas las generaciones fue de : ", poblacionFinal)
    print("La poblacion que permanecio viva en general fue de : ", ViViFINAL)
    print("La poblacion que paso de viva a muerta en general fue de  : ", ViMuFINAL)
    print("La poblacion que se mantuvo muerta en toda la simulacion fue de : ", MuMuFINAL)
    print("La poblacion que revivio en general con las esferas del dragon es de : ", MuViFINAL)
    print("══════════════════════════════════════════════════════════════════════")