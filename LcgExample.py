# pip install numpy
import numpy as np

a = 2 #multiplier
c = 4 #increment
m = 5 #mode
x = 3 # la semilla 
for i in range(1,30):
    c = c * i
    for j in range(1,2):
        m = m / i
        for k in range(1,2):
            x= (np.mod((a*x+c),m))*i
            print("valor random = {}".format(x))