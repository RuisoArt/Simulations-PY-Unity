
n = int(input('Escribe el numero maximo de iteraciones: '))
pi = 0

for i in range(0,n):

    if(i>=1):
        if(i%2 == 0):
            pi = pi + (1)/(i+2)
        elif(i%2 != 0):
            pi = pi - (1)/(i+2)
    else:
        pi = pi + (1)/(i+1)

print(pi*4)