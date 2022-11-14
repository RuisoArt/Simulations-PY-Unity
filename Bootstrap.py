import numpy as np
import random
import matplotlib.pyplot as plt

PopData = list()
random.seed(7)

for _ in range(1000):
    DataElement = 50*random.random()
    PopData.append(DataElement)

PopSample = random.choices(PopData, k=100)
PopSampleMean = list()

for _ in range(1000):
    SampleI = random.choices(PopData, k=100)
    PopSampleMean.append(np.mean(SampleI))

plt.hist(PopSampleMean)
plt.show()

MeanPopSampleMean = np.mean(PopSampleMean)
print(f"La media del estimador de Bootstrap es: {MeanPopSampleMean}")

MeanPopData = np.mean(PopData)
print(f"La media de la polacion es: {MeanPopData}")

MeanPopSample = np.mean(PopSample)
print(f"la media de la muestra simple aleatoria es: {MeanPopSample}")