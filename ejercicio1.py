# Ejercicio1
# A partir de los arrays x y fx calcule la segunda derivada de fx con respecto a x. 
# Esto lo debe hacer sin usar ciclos 'for' ni 'while'.
# Guarde esta segunda derivada en funcion de x en una grafica llamada 'segunda.png'

import numpy as np

x = np.linspace(0,2.,10)
fx = np.array([0., 0.0494, 0.1975, 0.4444, 0.7901,1.2346 , 1.7778, 2.4198, 3.1605, 4.])

h=2.0/10
#segunda derivada, donde y1 es el siguiente valor, y es el valor actual y yy es el valor anterior, las y recorreran la lista fx y el h se haya desde las diferencias equiespaciadas de x 

def seg(y, y1, yy):
    s=(1/h**2)*(y1-2*y+yy)
    return s
