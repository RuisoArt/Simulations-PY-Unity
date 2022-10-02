from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

a = 75
c= 0
m = 2 ** 31 - 1
x = 0.1
u = np.array([])
N = 100

for i in range(N):
    x = np.mod((a*x+c),m)
    u = np.append(u,x/m)
    print(u[i])

s = 20
Ns = N /s 

S = np.arange (0, 1, 0.05)
counts = np.empty(S.shape, dtype=int)

V = 0
for i in range(20):
    counts[i] = len(np.where((u >= S[i]) & (u < S[i]+ 0.05))[0])
    V = V + (counts[i] - Ns) ** 2/Ns 

print("R = ",counts) # cantidad de valores en cada uno de los segmentos
print("V = ",V)

Ypos = np.arange(len(counts))
plt.bar(Ypos,counts)
plt.show()

#calcular grados de libertas (numero de filas*numeros de columnas)
# n = (2-1)*(20-1) = 19
#buscar en la tabla la fila 19 en interseccion con la columna del grado de tolerancia => X^{2} (19,0.05) = (30.14)
my_image = Image.open("chi_cuadrado.png","r")
my_image.show()
my_image.close()
# como (14.8 < 30.14) aceptamos la hypothesis of uniformity NULA 
