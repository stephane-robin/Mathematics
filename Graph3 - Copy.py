# Function drawing

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
plt.xlim(0,2)
plt.ylim(-8,8)
x00=np.zeros(100)
y00=np.linspace(-8,8,100)
plt.title(r'$ y=x^3 $' r', $ y=(x-2)^3 $')
x0=np.linspace(0,2,100)
y0=np.zeros(100)

x=np.linspace(0,2,100)
y=np.sqrt(0.2/np.pi)*(np.exp((-x**2)/(4*0.2))-np.exp((-(x-2)**2)/(4*0.2))+2*np.exp((-(x-1)**2)/(4*0.2)))+(2*x-2)

plt.plot(x00,y00,'k',x0,y0,'k',linewidth=1)
plt.plot(x,y,'b',linewidth=2)
plt.show()

