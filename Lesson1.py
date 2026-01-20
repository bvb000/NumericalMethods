import numpy as np
from matplotlib import pyplot as plt

def dfxn(x,y):
    return -y/2+4*np.exp(-0.5*x)*np.cos(4.0*x)

def fxn(x):
    return np.exp(-0.5*x)*np.sin(4.0*x)

def int_eul(x,y,dx):
    return y+dx*dfxn(x,y)

def int_heun(x,y,dx):
    ystar=y+dx*dfxn(x,y)
    xp=x+dx
    return y+0.5*dx*(dfxn(x,y)+dfxn(xp,ystar))

x0=0.0
x1=10.0
dx=0.1
y0=0.0
e0=0.0

y_eu=y0
y_he=y0

eul_arr=[]
heun_arr=[]
n_arr=[]

n=1
x=x0

while (x<(x1-0.5*dx)):
    n=n+1
    y_eu=int_eul(x,y_eu,dx)
    y_he=int_heun(x,y_he,dx)
    x=x+dx
    y_sol=fxn(x)
    eul_arr.append(y_eu-y_sol)
    heun_arr.append(y_he-y_sol)
    n_arr.append(n)

plt.plot(n_arr,eul_arr)
plt.plot(n_arr,heun_arr)

plt.show()