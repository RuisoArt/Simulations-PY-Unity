import numpy as np
import matplotlib.pyplot as plt

N = 1000
n = 10
p = 0.5

p1 = np.random.binomial(n, p , N)
p2 = plt.hist(p1, density=True, alpha=0.8, histtype='bar', color='blue', ec='blue')
x = N

plt.figure()
plt.title('Binomial Function')

plt.subplot(2, 1, 1)
plt.plot(p1)
plt.ylabel('Random Numbers')
plt.xlabel('numbers')

plt.subplot(2, 1, 2)
plt.plot(p2)
plt.ylabel('gauss')
plt.xlabel('numbers')

plt.show()

