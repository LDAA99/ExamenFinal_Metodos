# Ejercicio5
# Resuelva el siguiente sistema acoplado de ecuaciones diferenciales 
# dx/dt = sigma * (y - x)
# dy/dt = rho * x - y -x*z
# dz/dt = -beta * z + x * y
# con sigma = 10, beta=2.67, rho=28.0,
# condiciones iniciales t=0, x=0.0, y=0.0, z=0.0, hasta t=5.0.
# Prepare dos graficas con la solucion: de x vs y (xy.png), x vs. z (xz.png) 
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


sigma=10
beta=2.67
rho=28
t=0
deltat=0.1
tmax=5.0
x=0.0
y=0.0
z=0.0

X=[x]
Y=[y]
Z=[z]

def dxdt(x, y): #me va a dar los nuevos valores de x
    a=sigma * (y - x)
    return a

def dydt(x, y, z): #los nuevos valores de y
    b=rho * x - y -x*z
    return b

def dzdt(z, x, y): #los nuevos valores de z
    c=-beta * z + x * y
    return c

#para determinar que no pase de 5.0 el tiempo, tmax/deltat=50

for i in range(50):
    equis=dxdt(X[i], Y[i])
    X.append(equis)
    #al estar acoplados
    ye=dydt(equis, Y[i], Z[i]) 
    Y.append(ye)
    zeta=dzdt(equis, ye, Z[i])
    Z.append(zeta)
    

plt.figure()
plt.plot(X, Y)
plt.savefig("xy.png")

plt.figure()
plt.plot(X, Z)
plt.savefig("xz.png")






