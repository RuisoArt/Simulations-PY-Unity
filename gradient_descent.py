import numpy as np
import matplotlib.pyplot as plt
import random

# Funcion derivada menos el gradiente de
def Gradf(x): return 2* x -2

x = np.linspace(-1, 3, 100) # min=-1 max=99
y = (x**2) - 2*x + 1

fig = plt.figure()

axdef = fig.add_subplot(1, 1, 1)
axdef.spines['left'].set_position('center')
axdef.spines['bottom'].set_position('zero')
axdef.spines['right'].set_color('none')
axdef.spines['top'].set_color('none')
axdef.xaxis.set_ticks_position('bottom')
axdef.yaxis.set_ticks_position('left')


plt.plot(x, y, 'r')
plt.show()

# Parametros de entradas
ActualX = 3                 #X0
LearningRate = 0.01         # Tamaño o longitud del paso
PrecisionValue = 0.000001   # Grado de precicion del valor 
PreviousStepSize = 1        # 
MaxIteration = 10000        # 
InterationCounter = 0       # 

while PreviousStepSize > PrecisionValue and InterationCounter < MaxIteration:
    PreviousX = ActualX
    ActualX = ActualX - LearningRate*Gradf(PreviousX) #Formula: Xn(n+1) = Xn - gamma*Gradient(Xn)
    PreviousStepSize = abs(ActualX - PreviousX)
    InterationCounter = InterationCounter + 1
    print("Number of iterations = ", InterationCounter,"\nActual value of x is: ",ActualX)

print("\n\n\n X value of f(x) minimum: ", ActualX)
