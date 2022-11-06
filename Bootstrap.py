import numpy as np
import random
import matplotlib.pyplot as plt

PopData = list()
random.seed(7)

for _ in range(1000):
    DataElement = random.random() * 50
    PopData.append(DataElement)

PopSample = random.choice(, k=100)

PopSampleMean = list()
for _ in range(1000):
    SampleI = random.choice(, k=100)
    PopSampleMean.append(SampleI)

plt.hist(PopSampleMean)
plt.show()