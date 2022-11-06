import random

# random.seed(1) # para una semilla fija

dados = []

for i in range(100):
    dados.append(random.randint(1,6))
print(dados)

# random.random() entre 0 y 1
# random.uniform(0,100) entre un rango
# random.randint(-100,100) solo numeros enteros 
# random.radrange(0,100, 5) el paso de numero a numero y con rango
# random.sample() saca muestras 
# random.choice(dados)
