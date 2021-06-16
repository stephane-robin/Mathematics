# Function drawing
# program written in Python 2.7

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np
import math

# Creating the function
def f(x):
	return x**0.5  # careful, need to change the function

def g(x):
	return x/2
	
# Designing the background
plt.figure(1)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
print "The graph will be drawn for a specific interval"
xm=input("Enter the minimum in this interval : ")
XM=input("Enter the maximum in the interval : ")
plt.title(r'$ y=\sqrt{x} , y=x/2 $')  # careful, need to change the function
x00=np.zeros((abs(xm)+XM)*10)  # computing y axis
y00=np.linspace(f(xm),f(XM),(abs(xm)+XM)*10)
x0=np.linspace(xm,XM,(abs(xm)+XM)*10) # computing x axis
y0=np.zeros((abs(xm)+XM)*10)
plt.plot(x00,y00,'k',x0,y0,'k',linewidth=1)

# Designing the function
x=np.linspace(xm,XM,(abs(xm)+XM)*10)
plt.plot(x,f(x),'r',linewidth=2)
X=np.linspace(xm,XM,(abs(xm)+XM)*10)
plt.plot(X,g(X),'g',linewidth=2)

plt.show()

