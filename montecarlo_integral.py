import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(2)

f= lambda x: x**2
a = 0.0
b= 3.0

NumSteps = 1000000
XIntegral = []
YIntegral = []

XRectangle = []
YRectangle = []

ymin = f(a)
ymax = ymin

for i in range(NumSteps):
  x = a + (b-a) * float(i)/NumSteps
  y = f(x)

  if y < ymin: ymin = y
  if y > ymax: ymax = y

A = (b-a) * (ymax - ymin)
N = 1000000
M = 0

for k in range(N):
  x = a + (b-a) * random.random()
  y = ymin + (ymax - ymin) * random.random()

  if y <= f(x):
    M += 1
    XIntegral.append(x)
    YIntegral.append(y)

  else:
    XRectangle.append(x)
    YRectangle.append(y)

NumericalIntegral = M/N * A
print('Numerical integration = ' + str(NumericalIntegral))

Xlin = np.linspace(a,b)
Ylin = []

for x in Xlin:
  Ylin.append(f(x))

plt.axis([0,b,0,f(b)])

plt.plot(Xlin, Ylin, color='red', linewidth='4')
plt.scatter(XIntegral, YIntegral, color='cyan', marker='.')
plt.scatter(XRectangle, YRectangle, color='blue', marker='.')

plt.title('Numerical Integration using Monte Carlo method')
plt.show()

# Iteracion
# teorema de limite central
# teorema de numeros grandes
# funciones de agregacion (mean, min, max)
# M/N * (Factor a multiplicar)