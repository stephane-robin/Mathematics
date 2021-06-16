# Euler method

# Importing useful packages
from matplotlib import pyplot as plt
import numpy as np
import os

# Defining the function solution
def x(t):
	return np.exp(-t**2)

# Designing the background
plt.figure(1)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.grid(True)
print "The graph will be drawn for a specific interval"
a=input("Please enter the minimum in this interval : ")
a=float(a)
b=input("Please enter the maximum in this interval : ")
b=float(b)
plt.title(r"$ x'=-2 t x $, Approximation by Euler's method")
xX=np.zeros((abs(a)+b)*10)  # designing x axis
yX=np.linspace(x(a),x(b),(abs(a)+b)*10)
xY=np.linspace(a,b,(abs(a)+b)*10) # designing y axis
yY=np.zeros((abs(a)+b)*10)
plt.plot(xX,yX,'k',xY,yY,'k',linewidth=1)

# Designing the function solution
t=np.linspace(a,b,(abs(a)+b)*10)
plt.plot(t,x(t),'g',linewidth=2)

# Designing the approximation
k=0
xk=1.
n=input("Please enter the number of iterations : ")

while k<n:
	plt.plot([(b-a)*k/n,(b-a)*(k+1)/n],[xk,xk*(1-2*k*((b-a)**2)/(n**2)-2*a*(b-a)/n)],'r')
	xk=xk*(1-2*k*((b-a)**2)/(n**2)-2*a*(b-a)/n)
	k=k+1

# Printing
plt.show()

