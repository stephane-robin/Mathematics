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
plt.xlim(-4,5)
plt.ylim(-5,5)
x00=np.zeros(100)
y00=np.linspace(-5,5,100)
plt.title(r'$ y=x^3 $' r', $ y=(x-2)^3 $')
x0=np.linspace(-4,5,100)
y0=np.zeros(100)

x1=np.linspace(-4,5,100)
y1=x1*x1*x1
x2=np.linspace(-4,5,100)
y2=(x2-2)*(x2-2)*(x2-2)
plt.plot(x00,y00,'k',x0,y0,'k',linewidth=1)
plt.plot(x1,y1,'b',x2,y2,'g',linewidth=4)
plt.show()

