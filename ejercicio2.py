# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
print(x)

for i in x:
    impar=i%2
    if(i>800):
        break
    elif(impar!=0):
        print(i)
        