# Function drawing
# This program draws several graphics in the same window. Each graphic is defined in several sequences
# Program written in Python 2.7

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np

# Designing the background
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.grid(True)
plt.xlim(-3,3)
plt.ylim(-1,2)

# Designing the functions
# Function of reference
x1=np.linspace(-3,-1.01,30)
y1=np.zeros(30)
x2=np.linspace(-0.99,0.99,200)
y2=np.exp(1/(x2*x2-1))
x3=np.linspace(1.01,3,30)
y3=np.zeros(30)
plt.plot(x1,y1,'b',x2,y2,'b',x3,y3,'b',linewidth=4)

u1=np.linspace(-3,-2.01,30)
v1=np.zeros(30)
u2=np.linspace(-1.99,1.99,200)
v2=np.exp(1/(u2*u2/4-1))
u3=np.linspace(2.01,3,30)
v3=np.zeros(30)
plt.plot(u1,v1,'r',u2,v2,'r',u3,v3,'r',linewidth=4)

# dilatation by 2
u1=np.linspace(-3,-0.51,30)
v1=np.zeros(30)
u2=np.linspace(-0.49,0.49,200)
v2=np.exp(1/(u2*u2*4-1))
u3=np.linspace(0.51,3,30)
v3=np.zeros(30)
plt.plot(u1,v1,'y',u2,v2,'y',u3,v3,'y',linewidth=4)

plt.show()
