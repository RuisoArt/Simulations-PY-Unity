#Dos dimensiones, lista dentro otra lista [matriz], para las 4 posibles trasiciones

estados_transicion = [["ViVi", "ViMu"], ["MuVi", "MuMu"]]

def bucle_calc_markov(ViVi, MuVi, MuMu, ViMu):
    TransitionMatrix = [[(ViVi / (ViVi + ViMu)), (ViMu / (ViVi+ ViMu))],
                        [(MuVi / (MuVi + MuMu)), (MuMu / (MuVi + MuMu))]]
    return TransitionMatrix

def finish_calc_markov(ViViFINAL,ViMuFINAL,MuMuFINAL,MuViFINAL):
    #Matriz de transicion
    TransitionMatrix = [[(ViViFINAL/(ViViFINAL+ViMuFINAL)),(ViMuFINAL/(ViViFINAL+ViMuFINAL))],
                        [(MuViFINAL/(MuViFINAL+MuMuFINAL)),(MuMuFINAL/(MuViFINAL+MuMuFINAL))]]
    return TransitionMatrix 
