from random import seed
from random import random
from matplotlib import pyplot as plt

seed(1)

RWPath = list()
RWPath.append(-1 if random() < 0.5 else 1)

for i in range(1, 1000):
    ZNValue  = -1 if random() < 0.5 else 1
    XNValue = RWPath[i-1] + ZNValue

    RWPath.append(XNValue)

plt.plot(RWPath)
plt.show()