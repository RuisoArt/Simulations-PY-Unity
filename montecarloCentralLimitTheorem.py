import numpy as np
import matplotlib.pyplot as plt
import random as random

a = 1
b = 100
N = 10000
DataPop = list(np.random.uniform(a, b, N))
plt.hist(DataPop, density=True, histtype='stepfilled', alpha=0.2)
plt.show()

SamplesMeans =[]

for i in range(N):
    DataExtracted = random.sample(DataPop, k=100)
    DataExtractedMean = np.mean(DataExtracted)
    SamplesMeans.append(DataExtractedMean)

plt.figure()
plt.hist(SamplesMeans, density=True, histtype='stepfilled', alpha=0.2)
plt.show()
