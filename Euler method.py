# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 22:00:23 2014

@author: stef
"""

# EULER'S METHOD TO SOLVE EDO
# ===========================

# PACKAGES
from matplotlib import pyplot as plt
import numpy as np

# INITIALISATION - it is necessary to change according to the project
n=100 # number of knots in the method
h=1./n # step for finite difference method

def f(a,b):
    return -2*a*b # it is necessary to change according to the project

# CREATING THE APPROXIMATED SOLUTION BY FINITE DIFFERENCE METHOD
u=list(range(0,n+1))
u[0]=1.

x=list(range(0,n+1))
x[0]=0.

for i in range(0,n):
    u[i+1]=u[i]+h*f(x[i],u[i])
    x[i+1]=x[i]+h
        
# PRINTING THE GRAPH
# Designing the background
plt.figure(1)
plt.xlabel("x")
plt.ylabel("u(x)")
plt.title("Resolution of $ u'(x)=-2 x u(x) $, by Euler's method, for $ x \in[0,1]$")
plt.grid(True)
plt.xlim(-0.2,1.2) # the interval of study is [0,1]
plt.ylim(-0.2,1.2)
Xx=np.linspace(-0.2,1.2,100) # drawing the X axis
Xy=np.zeros(100)
Yx=np.zeros(100) # drawing the Y axis
Yy=np.linspace(-0.2,1.2,100)
plt.plot(Xx,Xy,'k',Yx,Yy,'k',linewidth=1)

# Designing the theoretical solution in black
t=np.linspace(0,1,100)
ut=np.exp(-t**2)
plt.plot(t,ut,'k',linewidth=1)

# Designing the approximated solution
plt.plot(x,u,'b',linewidth=1)

plt.show()