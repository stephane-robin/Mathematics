# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:49:18 2015

@author: stef
"""

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib as plt
n=16
h=float(1/n)

x_i=np.zeros(n) 
for i in range(0,n):  
    x_i[i]=i*h

u=np.zeros(n) 
# i entre 0 et n-1
for i in range(0,n): 
    u[i]=0.1*(i*i/2-i)/3

v=np.zeros(n)
for i in range(0,n):
    v[i]=x_i[i]+u[i]

fig = figure()
ax = Axes3D(fig)
X = np.arange(0,1,h)
Y = np.arange(0,1,h)
X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#print(len(X))
Z = np.ones(n)#cos(R)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,color='yellow')
#ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cm.hot)
ax.set_zlim(-2,2)

# savefig('../figures/plot3d_ex.png',dpi=48)
show()

fig = figure()
ax = Axes3D(fig)
X = np.arange(0,1,h)
Y = np.arange(0,1,h)
v, Y = np.meshgrid(v, Y)
#R = np.sqrt(X**2 + Y**2)
#print(len(X))
Z = np.ones(n)#cos(R)
print(len(X))
ax.plot_surface(v, Y, Z, rstride=1, cstride=1,color='yellow')
#ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=cm.hot)
ax.set_zlim(-2,2)

show()

