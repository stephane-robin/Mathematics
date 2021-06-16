# Function drawing
# This program draws 2 graphics in 2 different windows

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np

# Designing the background


# Designing the functions
# Function of reference
plt.figure(1)
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.grid(True)
plt.xlim(-3,3)
plt.ylim(-1,2)
plt.title("graph1")
x1=np.linspace(-3,-1.01,30)
y1=np.zeros(30)
x2=np.linspace(-0.99,0.99,200)
y2=np.exp(1/(x2*x2-1))
x3=np.linspace(1.01,3,30)
y3=np.zeros(30)
plt.plot(x1,y1,'b',x2,y2,'b',x3,y3,'b',linewidth=4)

# dilatation by 1/2
plt.figure(2)
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.grid(True)
plt.xlim(-3,3)
plt.ylim(-1,2)
plt.title("graph2")
u1=np.linspace(-3,-2.01,30)
v1=np.zeros(30)
u2=np.linspace(-1.99,1.99,200)
v2=np.exp(1/(u2*u2/4-1))
u3=np.linspace(2.01,3,30)
v3=np.zeros(30)
plt.plot(u1,v1,'r',u2,v2,'r',u3,v3,'r',linewidth=4)

plt.show()

# dilatation by 2
