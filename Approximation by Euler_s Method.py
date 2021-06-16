# RESOLUTION OF A DIFFERENTIAL EQUATION BY EULER'S METHOD
# Program written in Python 2.7
# This program finds an approximation of the solution of a differential equation by Euler's method

# Import useful packages
from matplotlib import pyplot as plt
import numpy as np
import math as m
import os

# Parameters
def f(x,y) :
	return -2*x*y

x1=input('Please enter the initial value of x : ')
x1=float(x1)
y0=input('Please enter the initial condition y(0) : ')
y0=float(y0)
h=0.1 # step

# Designing the background
plt.figure(1)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
plt.xlim(-2,12)
plt.ylim(-2,3)
X00=np.zeros(100)
Y00=np.linspace(-2,3,100)
plt.title(r"Approximation by Euler's method")
X0=np.linspace(-2,12,100)
Y0=np.zeros(100)
plt.plot(X00,Y00,'k',X0,Y0,'k',linewidth=1)

# MAIN COMMAND
x=x1
y=y0
for k in range(0,101) :
	yp=y
	xp=x
	y=y+h*f(x,y)
	x=x+h
	plt.plot([xp,yp],[x,y],'r')
	print ("x",k,"=",x," / y",k+1,"=",y)
print (xp)
print (yp)
os.system("pause")

# Printing
plt.show()
