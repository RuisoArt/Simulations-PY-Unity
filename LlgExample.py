# pip install numpy
import numpy as np

a = 75 #multiplier
c = 0 #increment
m = (2**31) - 1 #mode
x = 0.1 # la semilla 
max_number = 10
min_number = 0

for i in range(1,100):
    x= np.mod((a*x+c),m)
    u = (x/m)*100
    u = u * max_number % ((max_number - min_number + 1) + min_number)
    print("valor random: {0:.2f}".format(u), " iteracion: {}".format(i+1))