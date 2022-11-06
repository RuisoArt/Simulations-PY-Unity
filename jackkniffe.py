import random
import statistics as sta
import matplotlib.pyplot as plt

# pupulation data
PopData = list()
N = 100

def CVCalc(data):
  """ Calculo del coeficiente de Variacion.
      data: Data de entradas 
  """
  return sta.stdev(data) / sta.mean(data)


# random seed **Semilla**
random.seed(5)

# elements, generador de N-random numbers
for _ in range(N):
  DataItems = random.random() * 10 #(0->10)
  PopData.append(DataItems)

# Calculo del coeficiente de variacion de PopulationData
CVPopData = CVCalc(PopData)
print(f'Coeficioente de variacion de PopulationData: {CVPopData}')

JackVal = list()
PseudoVal = list()

for _ in range(N - 1):
  JackVal.append(0)

for _ in range(N):
  PseudoVal.append(0)

# Recorre para N-Pseudo valores
for i in range(N):
  # Recorre para N-1 sub-sampling elementos
  for j in range(N-1):
    if (j<i):
      JackVal[j] = PopData[j]
    elif (j>i):
      JackVal[j-1] = PopData[j]
    
  # Calculo de la dispercion de la CV* u optima con resampling-CV
  PseudoVal[i] = N * CVPopData - (N-1)*CVCalc(JackVal)


# Graficos :

plt.hist(PseudoVal)
plt.show()

# valores finales

print(f'Mean: {sta.mean(PseudoVal)}')
print(f'Variance: {sta.variance(PseudoVal)}')
print(f'Jack Kniffe Variance: {sta.variance(PseudoVal) / N}')