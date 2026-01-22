import numpy as np
from matplotlib import pyplot as plt
    
def phi0(x): #fxn for t=0, 40<=x<=70
    if (x>=40 and x<=70):
        return np.sin(np.pi*((x-40.)/30.))**2
    else:
        return 0.0

def ftfs(phi_now): #forward time, forward space
    return (1+c)*phi_now-c*np.roll(phi_now,-1) 

def ftbs(phi_now): #forward time, backward space
    return (1-c)*phi_now+c*np.roll(phi_now,1)

dx=0.10 #0.10m
u=0.087 #0.087m/s
dt=dx/u #dt=dx/u for c=1, no damping
c=u*dt/dx #c=1
t=0 #0s initial t
t1=1000 #1000s final t
x0=0 #0m initial x
x1=100 #100m final x

x=np.arange(x0,x1,dx) #1D array of x-values between x0 and x1 with step nx
phi=[phi0(a) for a in x] #apply phi0 function to all x in array to fill phi array
phi=np.array(phi)

while (t<t1):
    if (u>0):
        phi_new=ftbs(phi) #ftbs is stable if u>0
    else:
        phi_new=ftfs(phi) #ftfs is stable if u<0
    phi=phi_new
    if (t==0) or (round(t)%200==0):
        print(t)
        plt.plot(x,phi, label='phi('+str(round(t))+'s)')
    t=t+dt

plt.xlabel('X')
plt.ylabel('phi(x)')
plt.legend( )
plt.show()