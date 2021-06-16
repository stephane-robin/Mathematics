# RESOLUTION OF A DIFFERENTIAL EQUATION BY RUNGE KUTTA'S METHOD
# Program written in Python 2.7
# This program finds an approximation of the solution of a differential equation by Runge Kutta's method

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
#plt.xlim(-2,12)
#plt.ylim(-2,3)
X00=np.zeros(10)
Y00=np.linspace(-2,3,10)
plt.title(r"Approximation by Runge Kutta's method")
X0=np.linspace(-2,12,10)
Y0=np.zeros(10)
plt.plot(X00,Y00,'k',X0,Y0,'k',linewidth=1)

# MAIN COMMAND
x=x1
y=y0
for k in range(0,101) :
	xp=x
	yp=y
	k1=f(x,y)
	k2=f(x+h/2,y+h/2*k1)
	k3=f(x+h/2,y+h/2*k2)
	k4=f(x+h,y+h*k3)
	y=y+h/6*(k1+2*k2+2*k3+k4)
	x=x+h
	plt.plot([xp,yp],[x,y],'r')
	print 'x',k,'=',x,' / y',k+1,'=',y

os.system("pause")

# Printing
plt.show()
