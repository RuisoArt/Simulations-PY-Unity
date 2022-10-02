# pip install numpy
#pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

a = 1                               #limite inferior del random
b = 100                             #limite superior del random
N = 1000000                         #numero de puntos
X1 = np.random.uniform(a, b, N)     #Generador de randoms uniformes

#grafica de numeros aleatorios
plt.plot(X1)
plt.show()

#grafica de funcion de desnidad PDF (Probability Density Function)
plt.figure()
plt.hist(X1, density=True, histtype='stepfilled', alpha=0.2)
plt.show()

    