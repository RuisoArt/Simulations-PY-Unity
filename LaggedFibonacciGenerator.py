from re import X
import numpy as np
import matplotlib.pyplot as plt

def original_fibonacci():
    n = int(input("Cuantos numeros quieres: "))

    x0, x1, x2 = 0,1,0
    array_y, array_x = [], []

    for i in range (0, n):
        x2 = x0 + x1
        x0 = x1
        x1 = x2
        array_y.append(x2)
        array_x.append(i)

    print(str(array_y))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(array_x, array_y, color='tab:blue')
    plt.show()

def randomXfibonacci():
    x0 = 1
    X1 = 1
    m = 2 ** 32
    for i in range(1,101):
        x = np.mod((x0 + X1),m)
        x0 = X1
        X1 = x
        print(x)



original_fibonacci()
#randomXfibonacci()
