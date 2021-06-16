# Function drawing
# This program draws 2 graphics in the same window
# program written in Python 2.7

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np

# Creating the function
def f(x):
	return x*x*x

def g(x):
	return (-x)*(-x)*(-x)

# Designing the background
plt.figure(1)
plt.xlabel("axe des x")
plt.ylabel("axe des y")
plt.grid(True)
print "The graph will be drawn for a specific interval"
xm=input("Enter the minimum in this interval : ")
XM=input("Enter the maximum in the interval : ")
ym=input("Enter the limit of the drawing for the y axis : ")
YM=input("Enter the limit of the drawing for the y axis : ")
plt.title(r'$ x^3 $, $ (-x)^3 $')  # careful, need to change the function
x00=np.zeros((abs(xm)+XM)*10)  # computing y axis
y00=np.linspace(f(xm),f(XM),(abs(xm)+XM)*10) # careful, need to change the function
x0=np.linspace(xm,XM,(abs(xm)+XM)*10)  #computing x axis
y0=np.zeros((abs(xm)+XM)*10)
plt.plot(x00,y00,'k',x0,y0,'k',linewidth=1)

# Designing the function
x=np.linspace(xm,XM,(abs(xm)+XM)*10)

x1=np.linspace(xm,XM,(abs(xm)+XM)*10)

plt.plot(x,f(x),'b',x1,g(x1),'g',linewidth=4)

plt.show()

