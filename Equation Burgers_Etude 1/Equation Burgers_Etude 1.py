# Burgers equation
# This program draws the classic solution for the Burgers equation in the 1st study of the lesson

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np

t=0
while t<1:
    # Graph_1
    # Frame
    plt.figure(1)
    plt.xlabel("x(t)")
    plt.ylabel("u(t,x)")
    plt.grid(True)
    plt.xlim(-3,3)
    plt.ylim(-3,3)
    plt.title("u(t,x)")
    # X axis
    Xabs=np.linspace(-3,3,100)
    Xord=np.zeros(100)
    # Y axis
    Yabs=np.zeros(100)
    Yord=np.linspace(-3,3,100)
    plt.plot(Xabs,Xord,'k',Yabs,Yord,'k',linewidth=1)
    # Function
    xa=np.linspace(-3,-1.1,100)
    ua=np.zeros(100)
    xb=np.linspace(-0.9,t,100)
    ub=(1.+xb)/(1.+t)
    xc=np.linspace(t,0.9,100)
    uc=(1.-xc)/(1.-t)
    xd=np.linspace(1.1,3,100)
    ud=np.zeros(100)
    plt.plot(xa,ua,'b',xb,ub,'b',xc,uc,'b',xd,ud,'b',linewidth=2)
    t=t+0.1
    plt.show()



